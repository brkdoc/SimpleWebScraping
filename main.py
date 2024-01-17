import requests
from bs4 import BeautifulSoup
import time

lastPrice = 0.0
def controlProduct():
    global lastPrice
    URL = "https://www.amazon.com.tr/Atomik-Al%C4%B1%C5%9Fkanl%C4%B1klar-James-Clear/dp/6052998385/ref=lp_12466381031_1_4?pf_rd_p=41dcc440-cec6-42fb-ae31-b40ea353f9d4&pf_rd_r=TAT66EK7PWE99K69210P&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    page = requests.get(URL, headers=headers)
    content = BeautifulSoup(page.content, 'html.parser')
    productName = content.find(id="productTitle").get_text().strip()
    productPrice = content.find(id="price").get_text()
    convertedPrice = float(productPrice[:-3].replace(".", "").replace(",", "."))

    if lastPrice != convertedPrice:
        print(productName, convertedPrice)

    lastPrice = convertedPrice

while(True):
    controlProduct()
    time.sleep(3)



