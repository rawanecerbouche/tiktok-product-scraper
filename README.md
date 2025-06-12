 # TikTok Product Scraper

This project automates the extraction of trending keywords from TikTok using Selenium.  
Then, it analyzes their relevance with Google Trends to identify potential winning products for e-commerce.
## project architecture
tiktok-trends/
├──README.md
├── main.py
├──.gitignore
├── requirements.txt
├── scraper/
│ ├── init.py
│ ├── tiktok_scraper.py
│ └── trends_analysis.py
└── data/
└── keywords.csv # created after running main.py
## Features
- Automated keyword collection from TikTok
- Trend analysis using Google Trends API
- Export to CSV for further analysis
- Modular architecture (easily extendable to Instagram, YouTube, etc.)
## skills
This project demonstrates skills in:
- Automated scraping (Selenium-ready)
- Google Trends API usage
- Data manipulation with pandas
- CSV export and modular code designls
## Technologies
- Python
- Selenium
- pytrends
- pandas
## remarque
Google Trends only allows 5 keywords per request, so this script sends keywords in batches.
TikTok or Google may change their website structure, which could break scraping.
For educational and testing purposes only.
Rate Limiting or Blocking – Google Trends may temporarily reject requests (e.g., error 429) if too many keywords are queried in a short time, or if the same IP is reused too often.
Anti-Bot Security – Both TikTok and Google implement security measures (e.g., CAPTCHA, JavaScript obfuscation, IP blocking) to detect and prevent automated scraping. This can cause the script to silently fail or return no data.




