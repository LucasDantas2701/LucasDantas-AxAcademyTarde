import traceback
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class User:
    def __init__(self, browser, selectors=None):
        self.browser = browser
        self.selectors = selectors or {}

    def _report_error(self, selector, e):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshot_{timestamp}.png"
        self.browser.save_screenshot(screenshot_name)

        with open("selenium_error_report.txt", "a") as f:
            f.write(f"[{timestamp}] Erro no selector: {selector}\n")
            f.write(f"Mensagem do erro: {str(e)}\n")
            f.write(traceback.format_exc())
            f.write(f"Screenshot: {screenshot_name}\n\n")

        print(f"[ERROR] Falha no selector {selector}. Detalhes salvos em {screenshot_name}")

    def find(self, selector, by=By.CSS_SELECTOR):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((by, selector))
            )

            print(f"Elemento encontrado: {selector}")
            return element
        except Exception as e:
            self._report_error(selector, e)
            return None

    def click(self, selector, by=By.CSS_SELECTOR):
        try:
            element = self.find(selector, by)
            if element:
                element.click()
        except Exception as e:
            self._report_error(selector, e)

    def type(self, selector, text, by=By.CSS_SELECTOR):
        try:
            element = self.find(selector, by)
            if element:
                element.clear()
                element.send_keys(text)
        except Exception as e:
            self._report_error(selector, e)

    def selectDropDOWN(self, selector, value, by=By.CSS_SELECTOR):
        try:
            element = self.find(selector, by)
            if element:
                Select(element).select_by_visible_text(value)
        except Exception as e:
            self._report_error(selector, e)

    def send_files(self, selector, path, by=By.CSS_SELECTOR):
        try:
            element = self.find(selector, by)
            if element:
                element.send_keys(path)
        except Exception as e:
            self._report_error(selector, e)

    def alert_accept(self):
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except Exception as e:
            self._report_error("alert", e)