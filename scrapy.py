from bs4 import BeautifulSoup
import requests

def get_url_input():
    url = input('What website would you like to scrape? Enter a URL: ')
    if not url:
        return None
    if 'www.' not in url:
        url = 'www.' + url
    if 'http' not in url:
        url = 'https://' + url
    return url

def fetch_website(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'lxml')
        else:
            print(f"Error: I cannot fetch from this site for now. {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

while True:
    url = get_url_input()
    if url is None:
        print('Please enter a valid URL')
        continue

    soup = fetch_website(url)
    if soup:
        print(soup.prettify())

    user_input = input('Do you want to scrape another website? (y/n) >')
    if user_input != 'y':
        break
print('Catch you later!')
