# 🌐 Selenium Web Scraper

This Python project uses Selenium and BeautifulSoup to scrape table data from [WebScraper.io](https://webscraper.io/test-sites/tables/tables-without-thead) and save the data in a timestamped CSV file.

## ✅ Features

- 📊 **Scrape Data from a table** — Extracts table data from the website.
- 💾 **Save to CSV** — Automatically saves scraped data in a CSV file with a timestamped filename.
- 🕒 **Timestamped Output** — Ensures each scrape creates a uniquely named file.
- 🌐 **JavaScript-Rendered Content** — Handles dynamic content that requires JavaScript.
- 🧮 **Runs Headless** — Operates in the background without opening a browser window.

## 🛠️ Tech Stack

- **Python 3**
- **Selenium** — To automate browser actions and render JavaScript.
- **BeautifulSoup (bs4)** — For parsing HTML content.
- **ChromeDriver** — To control Chrome in headless mode.

## 📁 Project Structure

```
python-web-scrapper/
│
├── webscrapper.py      # Main web scraping script
├── requirements.txt    # Python dependencies
├── chromedriver.exe    # ChromeDriver (ensure matching Chrome version)
└── .gitignore          # Files to ignore in version control
```

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Wannabeserbian/python-web-scrapper.git
cd python-web-scrapper
```

### 2️⃣ Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### 3️⃣ Download ChromeDriver

- Visit [ChromeDriver Downloads](https://developer.chrome.com/docs/chromedriver/downloads)
- Match the version with your installed Chrome browser.
- Place the `chromedriver.exe` in the project root or add its path to system PATH.

### 4️⃣ Run the Web Scraper

```bash
python app.py
```

The scraper will:

- Print the **page title** and **scraped data** in the terminal.
- Save the results in a CSV file named like: `scraped-data-YYYYMMDD-HHMM.csv`.
