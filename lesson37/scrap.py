import pprint

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    pass
    # response = requests.get('https://en.wikipedia.org/wiki/ChatGPT')
    # # print(response.text)
    #
    # soup = BeautifulSoup(response.text, 'html.parser')
    # # print(soup.get_text(strip=True))
    # all_p = soup.find_all('p')
    # body = soup.find("div", {'id': 'bodyContent'})
    # print(type(body))
    # print(body)
    # body.find_all('p')

    # response = requests.get('https://www.ikea.com/il/he/cat/tables-desks-fu004/')
    # soup = BeautifulSoup(response.text, 'html.parser')
    # i = soup.find_all('img', {'class': 'pip-image'})
    # print(i)
    # all_products = []
    # a = soup.find_all('div', {'class': 'pip-product-compact'})
    # for t in a:
    #     new_product = {
    #         'id': t.attrs['data-product-number'],
    #         'name': t.attrs['data-product-name'],
    #         'price': t.attrs['data-price']
    #     }
    #     all_products.append(new_product)
    #     img_tag = t.find('img', {'class': 'pip-image'})
    #     new_product['img_url'] = img_tag.attrs['src']
    # pprint.pprint(all_products)
    #

    # r = requests.get('http://pricesprodpublic.blob.core.windows.net/price/Price7290027600007-413-202303291340.gz?sv=2014-02-14&sr=b&sig=jH0VUIbeRTGSaQqA9ing6XPE7ioanj946LBxsBJTOno%3D&se=2023-03-29T11%3A40%3A48Z&sp=r')
