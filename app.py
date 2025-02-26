from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-accelerated-2d-canvas")
    chrome_options.add_argument("--disable-accelerated-jpeg-decoding")
    chrome_options.add_argument("--disable-accelerated-video-decode")
    chrome_options.add_argument("--disable-accelerated-mjpeg-decode")
    chrome_options.add_argument("--disable-3d-apis")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--disable-features=UseSkiaRenderer")
    chrome_options.add_argument("--disable-features=SurfaceSynchronization")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize driver
    driver_path = "chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Scrape the website


def scrape_trading_economics():
    url = "https://webscraper.io/test-sites/tables/tables-without-thead"
    driver = setup_driver()

    print(f"🌐 Navigating to {url}")
    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to load content

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

   # Finding table
    table = soup.find("table", class_="table table-bordered")

    if not table:
        print("❌ Could not find the table.")
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
