import requests
from bs4 import BeautifulSoup
import re
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def refined(s):
    return re.sub(r"\D+", "", s)


def write_csv(data):
    with open("plugins.csv", 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')

        writer.writerow((data['name'], data['url'], data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all('section', class_="plugin-section")[1]
    plugins = p1.find_all('article')
    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a')['href']
        rating = plugin.find('span', class_="rating-count").find('a').text
        r = refined(rating)
        data = {'name': name, 'url': url, 'rating': r}
        write_csv(data)


def main():
    url = 'https://ru.wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
