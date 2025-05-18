from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

driver = webdriver.Edge() # because its my default browser
driver.get("https://www.gramedia.com/categories/buku/fiksi-sastra/novel?is_available_only=true")

sleep(5)
cards           = list(driver.find_elements(By.CSS_SELECTOR, '[data-testid="productCardContent"]'))

result = []
for card in cards:
    title          = card.find_element(By.CSS_SELECTOR, '[data-testid="productCardTitle"]')
    final_price    = card.find_element(By.CSS_SELECTOR, '[data-testid="productCardFinalPrice"]')
    try:
        normal_price   = card.find_element(By.CSS_SELECTOR, '[data-testid="productCardSlicePrice"]')
        discount       = card.find_element(By.CSS_SELECTOR, '[data-testid="productCardDiscount"]')

        result.append({
            "title":title.text.strip(), 
            "normal_price" : normal_price.text.strip(),
            "discount" : discount.text.strip(), 
            "final_price":final_price.text.strip()})
    except:
        normal_price = "0"
        discount = "0"

        result.append({
            "title":title.text.strip(), 
            "normal_price" : normal_price,
            "discount" : discount, 
            "final_price":final_price.text.strip()})

# put the result in csv file
with open("result.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "normal_price", "discount", "final_price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)