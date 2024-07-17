import requests
from bs4 import BeautifulSoup


def scrape_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('a')
    news_list = []
    for headline in headlines:
        news_list.append(headline.text.strip())
    return news_list
if __name__ == "__main__":
    news_url = "https://lite.cnn.com/"
    headlines = scrape_news_headlines(news_url)
    print("Latest News Headlines:")
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}.{headline}")