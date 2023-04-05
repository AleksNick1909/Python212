# ПАРСИНГ данных с сайта (процесс автоматического сбора данных)
# pip instal beatifulsoup4 или bs4

# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find_all("div", class_="row")[2]
# # row = soup.find("div", class_="name")  # первый встретившийся элемент с class_="name"
# # row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# # row = soup.find_all("div", {"data-set": "salary"})
# # row = soup.find("div", string="Alena").parent
# # row = soup.find("div", string="Alena").find_parent(class_="row")
# # row = soup.find("div", id="whois3").find_next_sibling()   # найти следующего соседа
# row = soup.find("div", id="whois3").find_previous_sibling()   # найти предыдущего соседа
# print(row)


# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all("div", class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)


# *****
# import re
#
#
# def get_salary(s):
#     patter = r'\d+'
#     # res = re.findall(patter, s)[0]
#     res = re.search(patter, s).group()
#     print(res)
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)


# ****
# import requests
# from bs4 import BeautifulSoup
# import re
# import csv

# res = requests.get('https://ru.wordpress.org/')
# # print(res.headers['Content-Type'])
# # print(res.content)
# print(res.text)

# *****


# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")  # pip install lxml
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# ****

# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open("plugins.csv", 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('section', class_="plugin-section")[1]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         # url = plugin.find('h3').find('a').get('href')  # 1 sposob
#         url = plugin.find('h3').find('a')['href']   # 2 sposob
#         rating = plugin.find('span', class_="rating-count").find('a').text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# ******

# from bs4 import BeautifulSoup
# import requests
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8-sig') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active_install'], data['tests']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     element = soup.find_all('article', class_='plugin-card')
#     for el in element:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()  # strip удаляет пробельные символы
#         except ValueError:
#             snippet = ''
#
#         try:
#             active = el.find('span', class_='active-installs').text.strip()
#         except ValueError:
#             active = ''
#
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active_install': active,
#             'tests': cy
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(5):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# *****
from parse import Parser


def main():
    pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
    pars.run()


if __name__ == '__main__':
    main()

