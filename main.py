import requests
import time
from bs4 import BeautifulSoup

from mail import sendMail

# Set the URL you want to webscrape from
monthsCzech = ['Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen', 'Červenec', 'Srpen', 'Září', 'Říjen', 'Listopad', 'Prosinec']

wikiBase = "https://cs.wikipedia.org/wiki/Wikipedie:Vybraná_výročí_dne/"
wikiUrl = "https://cs.wikipedia.org/wiki/"

today = wikiBase + time.strftime("%d")+"._"+monthsCzech[int(time.strftime("%m"))-1].lower()
tomorrow = wikiBase + time.strftime("%d", time.localtime(time.time() + 24*3600))+"._"+monthsCzech[int(time.strftime("%m"))-1].lower()

emailBodySetToReset = ""

def LookUp(url, date, emailBody):

	
	print("Loading adress "+url)

	# Connect to the URL
	response = requests.get(url)

	# Parse HTML and save to BeautifulSoup object
	soup = BeautifulSoup(response.text, "html.parser")
	emailBody += "<h1>"
	emailBody += "Významná data z " + date
	emailBody += "</h1>"

	emailBody += "<br>"
	emailBody += "<br>"

	print("\n\t/********************/\n\n\tVýznamná data z "+date+" \n\n\t/********************/\n")

	CzDiv = soup.select_one(".mw-parser-output > ul:nth-child(2)")
	for cell in CzDiv.select('li'):
		#print("Událost:")
		emailBody += str(cell)
		emailBody += "<br>"

		print(cell.getText())
		print("\n")
	return emailBody

todayEvents = LookUp(today, time.strftime("%d.%m."), emailBodySetToReset)
tomorrowEvents = LookUp(tomorrow, time.strftime("%d.%m.", time.localtime(time.time() + 24*3600)), emailBodySetToReset)

allEvents = todayEvents.replace("/wiki/", wikiUrl) + tomorrowEvents.replace("/wiki/", wikiUrl)
sendMail(allEvents)