import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open("list.csv", 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')

        writer.writerow((data['name'], data['price'], data['url_img']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    for i in data:
        name = i.find("h4", class_="card-title").text.strip()
        price = i.find("h5").text.strip()
        url_img = "https://scrapingclub.com" + i.find('h4').find('a')['href']
        data = {'name': name, 'price': price, 'url_img': url_img}
        write_csv(data)


def main():
    for count in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        get_data(get_html(url))


if __name__ == '__main__':
    main()
