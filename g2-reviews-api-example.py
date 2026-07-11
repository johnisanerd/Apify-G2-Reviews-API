"""
G2 Reviews API: A Quick Start Example
See more at: https://apify.com/johnvc/g2-reviews-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/g2-reviews-api/input-schema?fpr=9n7kx3

This script shows how to call the G2 Reviews API on Apify from Python and read
its structured JSON output. It exercises several input parameters so you can see
what is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one product URL, maxReviewsPerProduct=5) to keep this
# first run inexpensive. Billing is per review returned, so a low cap keeps both
# volume and cost down. Raise these once you have your own API key and budget.
run_input = {
    "productUrls": ["https://www.g2.com/products/asana/reviews"],
    "maxReviewsPerProduct": 5,
    "sortBy": "recent",             # "", "recent", "helpful", "highest", "lowest"
    "includeProductMetadata": True,  # adds one product-metadata row per product
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/g2-reviews-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} row(s).\n")

# Show a few key fields from each row.
# Rows come in three shapes, distinguished by result_type:
#   "review"           - one collected review
#   "product_metadata" - a product-level row (present when includeProductMetadata is on)
#   "error"            - a validation or collection error row
for item in items:
    result_type = item.get("result_type")

    if result_type == "review":
        print(f"[review] {item.get('productName')} - {item.get('rating')} stars")
        print(f"  Title:   {item.get('title')}")
        print(f"  Role:    {item.get('reviewerRole')} | {item.get('companySize')}")
        print(f"  Date:    {item.get('datePublished')} | verified={item.get('verified')}")
        print(f"  Pros:    {item.get('pros')}")
        print(f"  Cons:    {item.get('cons')}")
        print(f"  Summary: {item.get('summary')}")
        print(f"  URL:     {item.get('reviewUrl')}")

    elif result_type == "product_metadata":
        print(f"[product] {item.get('productName')} - {item.get('category')}")
        print(f"  Star rating:  {item.get('starRating')} across {item.get('reviewCount')} reviews")
        print(f"  Competitors:  {item.get('competitors')}")

    elif result_type == "error":
        print(f"[error] {item.get('error_type')}: {item.get('error_message')}")

    print()
