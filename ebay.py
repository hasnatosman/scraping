#  TODO
# make a request to ebay.com and get a  page
# collect data from each details of the page
# collect lick to the detail of the page product
# save the collected data to a csv file
import csv
import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('Server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup
    # print(response.ok)
    # print(response.status_code)


def get_detail_data(soup):
    # title
    # price
    # items sold
    try:
        title = soup.find('h1', id='itemTitle').text[15:].replace('\xa0', '')

    except:
        title = ''
    # print(title)

    try:
        p= soup.find('span', id='prcIsum').text.strip()
        currency, price = p.split(' ')
    except:
        currency = ''
        price = ''

    # print(currency)
    # print(price)
    try:
        sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.split(' ')[0]
    except:
        sold = ''
    # print(sold)

    data = {
        'title': title,
        'currency': currency,
        'price': price,
        'total sold': sold

    }
    return data

def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    urls = [item.get('href') for item in links]
    return urls

def write_csv(data, url):
    with open('output.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        row = [data['title'], data['price'], data['currency'], data['total sold'], url]
        writer.writerow(row)




def main():
    url = 'https://www.ebay.com/sch/i.html?_nkw=men+watches&_pgn=1'
    product = get_index_data(get_page(url))

    for link in product:
        data = get_detail_data(get_page(link))
        write_csv(data, link)


if __name__ == '__main__':
    main()
