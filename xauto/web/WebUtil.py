from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class WebUtil:
    def __init__(self, proxy: str = None, extensions: list = []):
        chrome_options = webdriver.ChromeOptions()
        for ex in extensions:
            chrome_options.add_extension(ex)

        if proxy is not None:
            chrome_options.add_argument("--proxy-server=%s" % proxy)

        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def open(self, url: str):
        self.browser.get(url)

    def _find_element(self, xpath: str, second: int = 10):
        return WebDriverWait(self.browser, second).until(EC.presence_of_element_located((By.XPATH,
                                                                                         xpath)))

    def wait(self, xpath: str, second: int = 10):
        try:
            self._find_element(xpath, second)
        except Exception:
            pass

    def wait_multi(self, xpaths: list, second : int = 10):
        now = time.time()
        while time.time() - now < second:
            for x in xpaths:
                if self.browser.find_elements_by_xpath(x) is not None:
                    return
                time.sleep(0.1)

    def current_url(self):
        return self.browser.current_url

    def click(self, xpath: str):
        self._find_element(xpath).click()

    def input(self, xpath: str, text: str):
        self._find_element(xpath).send_keys(text)

    def clear(self, xpath: str):
        self._find_element(xpath).clear()

    def back(self):
        self.browser.back()

    def close_title(self, title):
        handles = self.browser.window_handles
        for handle in handles:
            self.browser.switch_to.window(handle)
            if self.title().find(title) >= 0:
                self.close_current_page()

    def title(self) -> str:
        return self.browser.title

    def close_current_page(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()

    def submit(self, xpath: str):
        self._find_element(xpath).submit()

    def switch_to_title(self, title):
        self.browser.switch_to.window(title)

    def ctrlw(self):
        self.browser.find_element_by_xpath('//body').send_keys(Keys.CONTROL + "w")

    def adblock_add_rule(self, rules = []):
        if rules is None or len(rules) == 0:
            return
        self.open("chrome-extension://gighmmpiobklfepjocnamgkkbiglidom/options.html")
        # click custom
        self.click('//*[@id="tabpages"]/ul/li[3]')
        # click edit
        self.click('//*[@id="btnEditAdvancedFilters"]')
        # click textarea
        textarea = self._find_element('//*[@id="txtFiltersAdvanced"]')
        for rule in rules:
            textarea.send_keys(Keys.ENTER)
            textarea.send_keys(rule)
        # save
        time.sleep(.2)
        self.click('//*[@id="btnSaveAdvancedFilters"]')

