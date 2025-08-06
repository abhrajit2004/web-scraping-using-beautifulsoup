import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'

def scrape_titles(url):
    r = requests.get(url)
    content = r.content
    # print(r.status_code)

    soup = BeautifulSoup(content, 'html.parser')

    with open('nytimes_titles.txt', 'w', encoding='utf-8') as f:
        for p in soup.find_all('p', class_='indicate-hover'):
            if len(p.text) != 0:
                title = p.text
                f.write(title + '\n')
                print(f"Title: {title}")
    
    

scrape_titles(url)