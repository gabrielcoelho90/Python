from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

GOOGLE_SHEET_LINK = ("https://docs.google.com/forms/d/e/1FAIpQLSc2tu6YI47ePuEh8-09j2WDRvf6uvgXWVrqjRruNs8KhpLB4Q"
                     "/viewform?usp=sf_link")

data = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response = data.text

soup = BeautifulSoup(response, "lxml")
a_elements = soup.select("div div a.property-card-link")
list_of_links = []
for a in a_elements:
    list_of_links.append(a.get("href"))

property_card_price = soup.select("div.PropertyCardWrapper span.PropertyCardWrapper__StyledPriceLine")
# print(property_card_price)
list_of_prices = []
for price in property_card_price:
    rent_per_month = price.getText()
    rent = rent_per_month.strip("+/mo 1bd")
    list_of_prices.append(rent)

print(list_of_prices)

property_card_addr = soup.select("a.StyledPropertyCardDataArea-anchor address")
list_of_addresses = []
for prop in property_card_addr:
    full_address = prop.getText().strip(" | \n ")
    list_of_addresses.append(full_address)


# filling the forms

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_SHEET_LINK)


for j in range(0, len(list_of_prices)):
    for i in range(0, 3):
        div_answers = driver.find_elements(By.CSS_SELECTOR, "div.rFrNMe.k3kHxc.RdH0ib.yqQS1.zKHdkd")
        time.sleep(0.5)
        div_answers[i].click()
        time.sleep(0.5)
        input_area = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
        if i == 0:
            input_area[i].send_keys(list_of_prices[j])
        if i == 1:
            input_area[i].send_keys(list_of_addresses[j])
        if i == 2:
            input_area[i].send_keys(list_of_links[j])
    send_button = driver.find_element(By.CSS_SELECTOR, "div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd")
    send_button.click()
    time.sleep(0.5)
    send_another_form = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another_form.click()
    time.sleep(0.5)




