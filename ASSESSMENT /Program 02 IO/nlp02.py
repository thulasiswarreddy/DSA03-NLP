
import re

products = [
    "Laptop", "Laptop Bag", "Smartphone",
    "Wireless Mouse", "Gaming Laptop",
    "Laptop Stand", "Keyboard"
]

def search_products(keyword, mode):
    patterns = {
        "exact": r"^" + re.escape(keyword) + r"$",
        "prefix": r"^" + re.escape(keyword),
        "suffix": re.escape(keyword) + r"$",
        "partial": re.escape(keyword)
    }

    matches = [
        p for p in products
        if re.search(patterns[mode], p, re.IGNORECASE)
    ]

    print("\nSearch Mode:", mode)
    print("Keyword:", keyword)
    print("Matching Products:", matches)
    print("Total Matches:", len(matches))

search_products("Laptop", "exact")
search_products("Laptop", "prefix")
search_products("Laptop", "suffix")
search_products("phone", "partial")
search_products("LAPTOP", "partial")
