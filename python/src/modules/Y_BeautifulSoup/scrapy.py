from src.utils.constants.url import URL as url
from bs4 import BeautifulSoup
import requests

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
cards = soup.select(".col-sm-4")



class Actions:
    def __init__(self, data:list):
        self.data = data
        self.items = []
    
    def build_item(self, button, name, price, link):
        return {
            "id": button.get("data-product-id"),
            "nome": name.get_text(strip=True),
            "preco": price.get_text(strip=True),
            "link": url + link.get("href")
        }
        
    def populate_item(self, item):
        self.items.append(item)

    def extrair(self):
        for card in self.data:     #passa por todos os cards 
             
            product_id = card.select_one("a.add-to-cart")               
            name = card.select_one(".col-sm-4 p")
            price = card.select_one(".col-sm-4 h2")
            link = card.select_one("div.choose a")
            if link:
                item = self.build_item(product_id, name, price, link)
                print(item)
                self.populate_item(item=item)