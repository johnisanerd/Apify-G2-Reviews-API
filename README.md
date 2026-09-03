# ⭐ G2 Reviews API: B2B Software Reviews to Structured JSON

> The most efficient, reliable, and developer-friendly way to use the G2 Reviews API.

**Actor page:** [apify.com/johnvc/g2-reviews-api](https://apify.com/johnvc/g2-reviews-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/g2-reviews-api/input-schema](https://apify.com/johnvc/g2-reviews-api/input-schema?fpr=9n7kx3)

Give it one or more G2 product review URLs and it returns one clean JSON row per review: rating, title, pros, cons, reviewer role, company size, and the publish date. Optionally add a product-metadata row per product with category, star rating, review count, and competitors. It is built API-first and MCP-ready, so you can call it from Python or drive it as a tool from an AI agent.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-G2-Reviews-API.git
   cd Apify-G2-Reviews-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python g2-reviews-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python g2-reviews-api-example.py
```

## Why Use This G2 Reviews API?

**A URL in, structured data out.** You never touch collection infrastructure. Pass one or more G2 product review URLs and get flat, predictable fields you can load straight into a sheet, a database, or a BI tool.

**One row per review.** Every review comes back with the same field shape: rating, title, pros, cons, reviewer role, company size, and the date it was published, plus a plain-language summary line.

**Pay per review.** Billing is per review returned, with no per-run setup fee, so you only pay for what is delivered. The `maxReviewsPerProduct` cap lets you control both volume and cost.

**Batch a whole competitive set.** Send many product URLs in one run to compare ratings and sentiment across products, by reviewer role and company size.

**Optional product metadata.** Turn on `includeProductMetadata` to add one product-level row per product, with category, star rating, review count, and competitors.

**Reliable and predictable.** A product with no reviews returns a clear message instead of failing the whole run, and a URL that cannot be collected returns an error row so one bad link never sinks the batch.

**MCP-ready.** Call it as a tool from Claude, Cursor, and other AI agents (see the install sections below).

## Features

### Core Capabilities
- Collect reviews from one or many G2 product review URLs (up to 100 per run)
- Cap reviews per product with `maxReviewsPerProduct` to control volume and cost
- Sort by most recent, most helpful, highest rated, or lowest rated
- Optional per-product metadata row with category, star rating, review count, and competitors

### Data Quality
- One consistent JSON row per review, every time
- A plain-language `summary` field on every review for quick scanning and AI use
- Clear error rows for URLs that cannot be collected, so a batch never fails as a whole

## Usage Examples

### Reviews for one product
```json
{
  "productUrls": ["https://www.g2.com/products/asana/reviews"],
  "maxReviewsPerProduct": 5
}
```

### Several products, most recent first, capped
```json
{
  "productUrls": [
    "https://www.g2.com/products/asana/reviews",
    "https://www.g2.com/products/trello/reviews"
  ],
  "maxReviewsPerProduct": 200,
  "sortBy": "recent"
}
```

### With product metadata
```json
{
  "productUrls": ["https://www.g2.com/products/asana/reviews"],
  "maxReviewsPerProduct": 50,
  "includeProductMetadata": true
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `productUrls` | `list[str]` | YES | - | One or more G2 product review URLs, for example `https://www.g2.com/products/asana/reviews`. A plain product URL without `/reviews` is accepted and normalized. Up to 100 per run. |
| `maxReviewsPerProduct` | `int` | No | `100` | Maximum reviews to return per product (1 to 1000). Caps cost and volume; each product is capped independently. |
| `sortBy` | `str` | No | `""` | Sort order for reviews. Empty for the default (most relevant), or one of `recent`, `helpful`, `highest`, `lowest`. |
| `includeProductMetadata` | `bool` | No | `false` | When enabled, add one product-metadata row per product (category, star rating, review count, competitors). Billed as a separate product-metadata event. |

## Output Format

Each review is returned as one JSON row:

```json
{
  "result_type": "review",
  "productName": "Asana",
  "rating": 4.5,
  "title": "Simple, team-friendly interface that keeps everyone productive",
  "reviewerRole": "Program Manager",
  "companySize": "Small-Business (50 or fewer emp.)",
  "datePublished": "2026-07-06",
  "summary": "4.5-star verified review of Asana from Program Manager: \"Simple, team-friendly interface\"",
  "verified": true,
  "reviewerName": "Jordan M.",
  "pros": "The interface is simple enough to learn quickly.",
  "cons": "More automations would be helpful in all plans.",
  "reviewUrl": "https://www.g2.com/products/asana/reviews/asana-review-13068232"
}
```

With `includeProductMetadata` enabled, each product also yields one metadata row:

```json
{
  "result_type": "product_metadata",
  "productName": "Asana",
  "productUrl": "https://www.g2.com/products/asana/reviews",
  "category": "Project Management",
  "starRating": 4.4,
  "reviewCount": 11000,
  "competitors": [{ "name": "Trello" }, { "name": "monday.com" }]
}
```

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the G2 Reviews API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/g2-reviews-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the G2 Reviews API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/g2-reviews-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/g2-reviews-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the G2 Reviews API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/g2-reviews-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/g2-reviews-api`, using OAuth when prompted.
5. Ask Claude to run the G2 Reviews API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/g2-reviews-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/g2-reviews-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the G2 Reviews API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/g2-reviews-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the G2 Reviews API to power your competitor analysis, customer sentiment, and review monitoring with reliable, structured results.*

Last Updated: 2026.09.03
