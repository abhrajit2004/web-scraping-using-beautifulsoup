import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

def scrape_quotes(url):
    r = requests.get(url)
    content = r.content
    # print(r.status_code)
    # print(r.text)

    soup = BeautifulSoup(content, 'html.parser')

    for quote in soup.find_all('span', class_='text'):
            author = quote.find_next('small', class_='author')
            tag = quote.find_next('meta', class_='keywords')
                 
            if author and tag:
                print(f"Quote by {author.text}: {quote.text} with tags {tag['content']}")
            else:
                return "No author or tag found."

scrape_quotes(url)