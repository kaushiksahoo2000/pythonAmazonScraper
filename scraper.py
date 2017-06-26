import requests
import pprint
import re
import unicodedata
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/GNARBOX-Portable-Backup-Editing-System/dp/B01NB0Q9QP'

def hello_world():
	return 'Hello World'
# def gbx():
# 	r = requests.get(URL)
# 	soup = BeautifulSoup(r.text, 'html.parser')
# 	columnHolder = []
# 	productDetails = {}
# 	additionalInformation = {}
# 	for row in soup.find_all('tr'):
# 		cols = [e.text for e in row.find_all('td')]
# 		if cols:
# 			columnHolder.append(cols)
# 	for col in columnHolder:
# 		productDetails[col[0]] = col
# 	print('PRINTINGGGG PRODUCT DETAILS')
# 	cleanfont = unicodedata.normalize('NFKD', productDetails['Best Sellers Rank'][1]).encode('ascii','ignore')
# 	print(type(cleanfont))
# 	whitespace = "\r\n\t"
# 	print(cleanfont.strip(whitespace))
# 	additionalInformation['Customer Reviews'] = unicodedata.normalize('NFKD', productDetails['Customer Reviews'][1]).encode('ascii','ignore').strip(whitespace)
# 	additionalInformation['Amazon Launchpad'] = unicodedata.normalize('NFKD', productDetails['Best Sellers Rank'][1]).encode('ascii','ignore').strip(whitespace)
# 	# pprint.pprint(additionalInformation)
# 	return additionalInformation

def gbx():
	r = requests.get(URL)
	soup = BeautifulSoup(r.text, 'html.parser')
	columnHolder = []
	productDetails = {}
	additionalInformation = {}

	for row in soup.find_all('tr'):
		cols = [e.text for e in row.find_all('td')]
		colscols = [x.strip(' ') for x in cols]
		if cols:
			columnHolder.append(colscols)
	for col in columnHolder:
		xcol = [y.strip(' ') for y in col]
		productDetails[xcol[0]] = xcol
	for idx, val in enumerate(productDetails['Customer Reviews']):
		if idx == 1:
			cleanfont = unicodedata.normalize('NFKD', val).encode('ascii','ignore')
			additionalInformation['Customer Reviews'] = cleanfont.translate(None, ' \n\t\r')
	for idx2, val2 in enumerate(productDetails['Best Sellers Rank']):
		if idx2 == 1:
			cleanfont2 = unicodedata.normalize('NFKD', val2).encode('ascii','ignore')
			additionalInformation['Amazon Launchpad'] = cleanfont2.translate(None, ' \n\t\r')
	return additionalInformation
