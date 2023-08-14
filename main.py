import requests
from bs4 import BeautifulSoup


def scrape_articles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    session = requests.Session()
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_div = soup.find('div', id='chr-content')

        if article_div:
            articles = article_div.find_all('h2', class_='article-title')

            with open('articles.txt', 'w') as file:
                for article in articles:
                    title = article.text.strip()
                    file.write(title + '\n')

            print(f"{len(articles)} articles scraped and saved to 'articles.txt'.")
        else:
            print("No articles found within the specified div.")
    else:
        print("Failed to fetch the webpage.")


if __name__ == "__main__":
    target_url = "https://#"  # Replace
    scrape_articles(target_url)