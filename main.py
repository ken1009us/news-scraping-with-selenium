import requests as re
import time

from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver')


def get_news():
    url = "https://www.nbcnews.com/health"
    page = re.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    content = soup.find_all('h2', class_="wide-tease-item__headline")
    lst = [str(news).split('>')[1].split('<')[0].strip() for news in content]

    return lst


def get_news_with_selenium():
    url = "https://www.nbcnews.com/health"
    driver.get(url)
    time.sleep(3)
    news_lst = []

    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content = soup.find_all('h2', class_="wide-tease-item__headline")
        news_lst.extend([str(news).split('>')[1].split('<')[0].strip() for news in content])

        try:
            print("==========Check if 'Load More' button is present==========")
            load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
            load_more_button.click()
            print("......")
            print("...")
            print(".")
            time.sleep(3)
        except:
            print("......")
            print("...")
            print(".")
            print("==========Completed!==========")
            break

    return news_lst


def print_news_title(news_lst):
    for title in news_lst:
        print(title)


def write_to_txt(news_lst):
    p = Path('.')
    text_file_path = p / 'data' / 'news-headlines.txt'

    with open(text_file_path, 'w') as fp:
        for item in news_lst:
            fp.write("%s\n" % item)
        print('Done!')



def main():
    news_list = get_news_with_selenium()
    write_to_txt(news_list)


if __name__ == '__main__':
    main()