import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

PRODUCT_URL_CSV = "products.csv"
SAVE_TO_CSV = True
PRICES_CSV = "prices.csv"
SEND_MAIL = True

def process_products(df):
    updated_products = []
    for product in df.to_dict("records"):
        html = get_response(product["url"])
        product["price"] = get_price(html)
        product["alert"] = product["price"] < product["alert_price"]
        updated_products.append(product)
    return pd.DataFrame(updated_products)

def get_response(url):
	response = requests.get(url)
	return response.text

def get_price(html):
	soup = BeautifulSoup(html, "lxml")
	el = soup.find(property="product:price:amount")
	elm = el["content"]
	price = float(elm)
	return price
