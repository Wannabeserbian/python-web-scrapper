from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import os

# Setup Selenium Chrome Driver


def setup_driver():
    chrome_options = Options()
    # Run in headless mode (no browser window)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    # Replace with the path to your chromedriver if not in PATH
    driver_path = "chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Scrape the website


def scrape_trading_economics():
    url = "https://tradingeconomics.com/country-list/rating"
    driver = setup_driver()

    print(f"🌐 Navigating to {url}")
    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to load content

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Find the table with the country ratings
    table = soup.find(
        "table", id="ctl00_ContentPlaceHolder1_ctl01_ctl01_GridView1")

    if not table:
        print("❌ Could not find the country ratings table.")
        return

    # Extract table headers
    headers = [header.text.strip() for header in table.find_all('th')]
    print("✅ Table Headers:", headers)

    # Extract table rows
    data_rows = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        cells = [cell.text.strip() for cell in row.find_all("td")]
        if cells:
            data_rows.append(cells)

    print(f"✅ Extracted {len(data_rows)} rows of data.")

    # Save to CSV
    timestamp = time.strftime("%Y%m%d-%H%M")
    filename = f"scraped-data-{timestamp}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data_rows)

    print(f"📁 Data saved to {filename}")


if __name__ == "__main__":
    scrape_trading_economics()
