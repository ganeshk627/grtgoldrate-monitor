import time

from playwright.sync_api import sync_playwright
import csv
from datetime import datetime
import re

import email_config
from send_email import  send_mail
import json


# Function to scrape data
def scrape_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # XServer need to run headed
        # page = browser.new_page()
        context = browser.new_context(
            geolocation={"longitude": 79.7460756, "latitude": 11.7508642},
            permissions=["geolocation"]
        )
        page = context.new_page()

        # with open('cookies.json', 'r') as f:
        #     cookies = json.load(f)
        #     page.context.add_cookies(cookies)

        page.set_viewport_size({"width": 1600, "height": 1200})

        # Visit website (replace URL with your target site)
        page.goto('https://www.grtjewels.com/')
        page.screenshot(path="screenshot.png", full_page=False)
        time.sleep(5)

        gold24 = page.query_selector('//li[contains(text(),"GOLD - 24k -")]').inner_text()
        gold22 = page.query_selector('//li[contains(text(),"GOLD - 22k -")]').inner_text()
        gold18 = page.query_selector('//li[contains(text(),"GOLD - 18k -")]').inner_text()
        platinum = page.query_selector('//li[contains(text(),"PLATINUM -")]').inner_text()
        silver = page.query_selector('//li[contains(text(),"SILVER -")]').inner_text()

        # cookies = page.context.cookies()
        # with open('cookies.json', 'w') as f:
        #     json.dump(cookies, f)

        subject = f'GRT Gold Rate Today - {datetime.now().strftime("%d/%m/%Y")}'
        body = f'\n\t{gold24}\n\t{gold22}\n\t{gold18}\n\t{platinum}\n\t{silver}'
        email_config.body = body
        print(subject, body)
        send_mail(body=body, subject=subject, screenshots=None)

        gold24price = re.search(r'Rs(\d+)', gold24).group(1)
        gold22price = re.search(r'Rs(\d+)', gold22).group(1)
        gold18price = re.search(r'Rs(\d+)', gold18).group(1)
        platinumprice = re.search(r'Rs(\d+)', platinum).group(1)
        silverprice = re.search(r'Rs(\d+)', silver).group(1)


        # Save data to CSV
        with open('grt_rates.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), gold24price, gold22price, gold18price, platinumprice, silverprice])

        browser.close()

if __name__ == "__main__":
    scrape_data()