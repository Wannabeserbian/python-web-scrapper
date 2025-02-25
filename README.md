# 🌐 Web Scraper for Country Ratings

This Python project is a **web scraper** that extracts **country ratings** from [Trading Economics](https://tradingeconomics.com/country-list/rating) and stores the data in a timestamped **CSV file**.

## ✅ Features

- 📊 **Scrape Country Ratings** — Extracts country rating data from the website.
- 💾 **Save to CSV** — Automatically saves scraped data in a CSV file with a timestamped filename.
- 🕒 **Timestamped Output** — Ensures each scrape creates a uniquely named file.
- 📋 **Prints Progress** — Displays extracted headers and data rows in the console.

## 🛠️ Tech Stack

- **Python 3**
- **Requests** — For making HTTP requests to the target website.
- **BeautifulSoup (bs4)** — For parsing HTML content.
- **CSV Module** — For writing the scraped data to a CSV file.
- **Time Module** — For generating timestamps.

## 📁 Project Structure

\`\`\`
webscrapper/
│
├── webscrapper.py # Main web scraping script
├── requirements.txt # Python dependencies
└── .gitignore # Files to ignore in version control
\`\`\`

## ⚡ Getting Started

### 1️⃣ Clone the Repository

\`\`\`bash
git clone <repository-url>
cd webscrapper
\`\`\`

### 2️⃣ Install Dependencies

Make sure you have Python installed, then run:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3️⃣ Run the Web Scraper

\`\`\`bash
python webscrapper.py
\`\`\`

The scraper will:

- Print the **page title** and **scraped data** in the terminal.
- Save the results in a CSV file named like: \`scraped-data-YYYYMMDD-HHMM.csv\`.

## 📊 Example CSV Output

\`\`\`
Country, Rating, Outlook
United States, AAA, Stable
Germany, AAA, Negative
Japan, A+, Stable
...
\`\`\`
