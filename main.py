import requests
from bs4 import BeautifulSoup
import random

user_agents =[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    ]

request_headers = {
    'user-agent': random.choice(user_agents)
}
 


url = 'https://www.wineenthusiast.com/region/us/'
response = requests.get(url, headers=request_headers)
soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find_all('div', class_='list')
print(soup.prettify())

# wine_elements = results.find_all("div", class_='list')
# for wine_element in wine_elements:
#    print(wine_element, end='\n'*2)

# print(response.text)