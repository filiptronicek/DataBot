import requests
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
monthsCzech = ['Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen', 'Červenec', 'Srpen', 'Září', 'Říjen', 'Listopad', 'Prosinec']

wikiBase = "https://cs.wikipedia.org/wiki/Wikipedie:Vybraná_výročí_dne/"

today = wikiBase + time.strftime("%d")+"._"+monthsCzech[int(time.strftime("%m"))-1].lower()
tomorrow = wikiBase + time.strftime("%d", time.localtime(time.time() + 24*3600))+"._"+monthsCzech[int(time.strftime("%m"))-1].lower()



def LookUp(url, date):

	
	print("Loading adress "+url)

	# Connect to the URL
	response = requests.get(url)

	# Parse HTML and save to BeautifulSoup object
	soup = BeautifulSoup(response.text, "html.parser")
	print("\n\t/********************/\n\n\tVýznamná data z "+date+" \n\n\t/********************/\n")

	CzDiv = soup.select_one(".mw-parser-output > ul:nth-child(2)")
	for cell in CzDiv.select('li'):
		#print("Událost:")
		print(cell.getText())
		print("\n")

LookUp(today, time.strftime("%d.%m."))
LookUp(tomorrow, time.strftime("%d.%m.", time.localtime(time.time() + 24*3600)))