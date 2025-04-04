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
	for product in df.to_dict("records"):
		# product["url"] is the URL

def get_response(url):
	response = requests.get(url)
	return response.text

def get_price(html):
	soup = BeautifulSoup(html, "lxml")
	el = soup.select_one(".sale-price")
	price = Price.fromstring(el.text)
	return price.amount_float
