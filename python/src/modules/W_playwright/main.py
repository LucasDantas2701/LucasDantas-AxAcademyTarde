from playwright.sync_api import sync_playwright
from src.utils.constants.url import URL
from src.modules.W_playwright.functions import User

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    user = User(page)

    # acessa a página de produtos
    user.goTo(URL)

    cards = user.find("div.features_items > div.col-sm-4")
    cards.first.wait_for(timeout=10000)  # espera o primeiro card aparecer

    for i in range(cards.count()):
        card = cards.nth(i)
        button = card.locator("a.add-to-cart").nth(0)
        button.wait_for(timeout=5000)
        product_id = button.get_attribute("data-product-id")

        name = card.locator("p").nth(0).inner_text()
        price = card.locator("h2").nth(0).inner_text()
        link = card.locator("div.choose a").nth(0).get_attribute("href")

        if link:
            item = {
                "id": product_id,
                "nome": name,
                "preco": price,
                "link": link
            }
            print(item)

    browser.close()