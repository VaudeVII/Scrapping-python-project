from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
#essentials
browser = webdriver.Chrome()
target_url = "https://scrapingsandbox.com/data-table"
browser.get(target_url)
pages = int(input("enter a number for how many pages you want"))
repeated_stuff = 0
product_information = []
#star of the show, movin and extractin
try:
    while repeated_stuff < pages:
        next_page_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-slot='button']:has(svg.lucide-chevron-right)")))

        product_name = [pname.text for pname in browser.find_elements(By.CSS_SELECTOR, 'a[href^="/product/"]')]
        product_category = [pcategory.text for pcategory in browser.find_elements(By.CSS_SELECTOR, '[data-slot="badge"]')]
        product_price = [pprice.text for pprice in browser.find_elements(By.CSS_SELECTOR, '[data-slot="table-cell"]')]
        product_rating = [prating.text for prating in browser.find_elements(By.CSS_SELECTOR, 'span.text-xs:not(.text-terminal-green)')]
        product_availability = [pavailability.text for pavailability in browser.find_elements(By.CSS_SELECTOR, 'span.text-xs.text-terminal-green')]

        product_information.extend([{"name": n, "category": c, "price": p, "rating": r, "availability": a} for n, c, p, r, a in zip(product_name, product_category, product_price, product_rating, product_availability)])
        repeated_stuff += 1

        if repeated_stuff < pages:
            next_page_button.click()

finally:
    browser.quit()

#finally saving
with open("extractedinfoproducts.json", "w", encoding="utf-8") as f:
    json.dump(product_information, f, indent=4) 

with open("extractedinfoproducts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "category", "price", "rating", "availability"])
    writer.writeheader()
    writer.writerows(product_information)