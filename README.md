# Product Scraper

A small Python + Selenium script that scrapes product info from a paginated table and saves it as CSV and JSON. I built it for practice on [Scraping Sandbox](https://scrapingsandbox.com/data-table), a site made for learning scraping.

## What it grabs

For every product: name, category, price, rating, and availability.

## How it works

You tell it how many pages to scrape, and it clicks through them one by one, collects everything into a single list, and writes it out to two files:

- `extractedinfoproducts.csv`
- `extractedinfoproducts.json`

## What you need to run it

- Python
- Google Chrome
- Selenium

## Setup

1. Install [Python](https://www.python.org/downloads/) and [Chrome](https://www.google.com/chrome/next-steps.html) if you don't have them.
2. Install Selenium by typing this in the terminal:

```bash
   py -m pip install selenium
```

3. Clone or download this repo.

## Running it

```bash
py pythonscraping.py
```

It'll ask how many pages you want. Type a number and let it run. The two output files show up in the same folder as the script, and you can open them right in your code editor.

## Sample output

CSV:

```csv
name,category,price,rating,availability
Lightweight Probiotics,Health,$155.62,4,Yes
Wireless LED Desk Lamp,Electronics,$145.40,4.6,Yes
Deluxe Tea Collection,Food & Beverage,$185.01,No,Yes
```

JSON:

```json
[
    {
        "name": "Lightweight Probiotics",
        "category": "Health",
        "price": "$155.62",
        "rating": "4",
        "availability": "Yes"
    },
    {
        "name": "Wireless LED Desk Lamp",
        "category": "Electronics",
        "price": "$145.40",
        "rating": "4.6",
        "availability": "Yes"
    }
```

## Need something similar?

If you need something similar for a different site or different fields, message me.
