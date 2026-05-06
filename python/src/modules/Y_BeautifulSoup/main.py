from src.modules.Y_BeautifulSoup.scrapy import Actions as Action, cards
from src.modules.Y_BeautifulSoup.data_handler import DataHandler

def main():
    action = Action(cards)
    action.extrair()
    items = action.items
    data_handler = DataHandler(data=items)
    data_handler.save()

if __name__ == "__main__":
    main()