from playwright.sync_api import sync_playwright
import csv
from datetime import datetime
import re

import email_config
from send_email import  send_mail


# Function to scrape data
def scrape_data():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Visit website (replace URL with your target site)
        page.goto('https://www.grtjewels.com/')

        # Scrape the data (replace with your selectors)
        gold24 = page.query_selector('//li[contains(text(),"GOLD - 24k -")]').inner_text()
        gold22 = page.query_selector('//li[contains(text(),"GOLD - 22k -")]').inner_text()
        gold18 = page.query_selector('//li[contains(text(),"GOLD - 18k -")]').inner_text()
        platinum = page.query_selector('//li[contains(text(),"PLATINUM -")]').inner_text()
        silver = page.query_selector('//li[contains(text(),"SILVER -")]').inner_text()

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