# NBC News Health Scraper

This Python script scrapes the headlines from the NBC News Health section using two different methods: one using the requests library and BeautifulSoup, and the other using Selenium with a headless Chrome browser.

## Prerequisites

Make sure you have the following installed:

```
Python 3.x
`requests` library
`BeautifulSoup` library
`pathlib` module
`Selenium` library
Chrome browser
ChromeDriver
```

## Installation

1. Clone the repository or download the script file.
2. Install the required libraries by running the following command:
```bash
pip install -r requirements.txt
```

3. Download the appropriate version of ChromeDriver for your Chrome browser version and place it in the same directory as the script. You can download ChromeDriver from the official site: ChromeDriver - WebDriver for Chrome


## Usage

To run the script, execute the following command:

```bash
python main.py
```

The script will scrape the headlines from the NBC News Health section using both methods. It will then save the headlines to a text file named news-headlines.txt in the data directory.

## How It Works

The script uses the requests library and BeautifulSoup to scrape the headlines from the NBC News Health section. It sends an HTTP GET request to the URL and parses the HTML response to extract the headlines.

The script also utilizes Selenium with a headless Chrome browser to scrape the headlines. It uses the ChromeDriver executable to launch the browser and navigates to the NBC News Health section. It continuously clicks the "Load More" button until all the headlines are loaded. It then extracts the headlines using BeautifulSoup from the HTML source of the page.

The extracted headlines are stored in a list and printed to the console. Additionally, the headlines are written to a text file named news-headlines.txt in the data directory.

## Customization
You can modify the script according to your needs:

- You can change the target URL by modifying the url variable in the get_news() and get_news_with_selenium() functions.
- You can adjust the waiting time between interactions with the page by changing the time.sleep() values in the get_news_with_selenium() function.
- You can modify the file path and name in the write_to_txt() function to save the text file in a different location or with a different name.

Feel free to explore and customize the script to suit your requirements.

## Disclaimer

This script is intended for educational purposes only. Scraping websites may violate their terms of service. Make sure to check the website's policies and obtain proper permission before scraping any data.

## Credits

Author: Shu-Hao Wu
Email: shwu2@illinois.edu