import requests
from bs4 import BeautifulSoup
from time import sleep

testflight_id = "https://testflight.apple.com/join/q1cg7IPl"
CHAT_ID = "-1001597696937" 
BOT_TOKEN = "5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI"
if len(testflight_id)==8:
	url = "https://testflight.apple.com/join/" + testflight_id
else:
	url = testflight_id
while True:
    site = requests.get(url)
    soup = BeautifulSoup(site.content,"html.parser")
    beta_status = soup.find("div",class_="beta-status").span.text
    if beta_status != "Esta versión beta está llena." or "This beta version is full.":
        BOT_URL = "https://api.telegram.org/bot{}/sendMessage".format(BOT_TOKEN)
        message = "You can finally join the beta. Hooooray. \b" + url
        requests.get(BOT_URL, params={"chat_id": CHAT_ID, "text": message,"parse_mode": "html", "disable_web_page_preview": "true"})
    else:
        print("Sadly the beta program is still full. Patience is a virtue so wait a bit longer. ")
    sleep(5)
