class User:
    def __init__(self, page, selectors=None):
        self.page = page
        self.selectors = selectors or {}

    def find(self, selector):
        return self.page.locator(selector)

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)
        
    def goTo(self, url):
        self.page.goto(url)
        
    def locator(self, selector):
        return self.page.locator(selector)