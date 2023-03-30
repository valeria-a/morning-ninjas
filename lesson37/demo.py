import re

from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://www.practicepython.org/exercises/"
    html_doc = requests.get(url).content
    # print(html_doc)
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())
    #
    # a_tags = soup.find_all("a")
    # print(a_tags)

    # header = soup.find("div", {'class': 'header'})
    # print(type(header))
    # print(header)
    # print(header.name)
    # print(header.attrs)

    # re.findall(r"/exercise/.*", "/exercise/2014/01/29/01-character-input.html")
    all_a = soup.find_all("a", attrs=dict(href=re.compile("/exercise/.*")))
    print(all_a[0].attrs['href'])