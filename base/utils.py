import requests
import lxml
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.mail import EmailMessage


def linkParser(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
        "Accept-Language": "en",
    }

    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.text, 'lxml')

    title = soup.find(id="itemTitle").getText().replace('Details about', '')
    price = soup.find('span', {'class': 'notranslate'}).getText().replace(',', '')

    currency = ['US', 'C', 'UK', 'EUR', 'PHP', 'zł']
    currency_sign = ['$', '£']

    for c in currency:
        if c in price:
            price = price.replace(c, '')

    for s in currency_sign:
        if s in price:
            price = price.replace(s, '')

    title = title.strip()
    price = float(price.strip())

    return title, price

