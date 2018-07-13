from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
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

    def wait(self, xpath: str, second: int = 15) -> bool:
        try:
            WebDriverWait(self.browser, second).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except Exception:
            return False

    def wait_do(self, xpath:str, func, *args):
        self.wait(xpath)
        func(xpath, *args)

    def wait_not_exist(self, xpath: str, timeout=10) -> bool:
        now = time.time()
        while time.time() - now < timeout:
            try:
                self.browser.find_element_by_xpath(xpath)
                time.sleep(0.1)
            except Exception:
                return True
        return False

    def wait_multi(self, xpaths: list, second: int = 10):
        now = time.time()
        while time.time() - now < second:
            for x in xpaths:
                if self.browser.find_elements_by_xpath(x) is not None:
                    return True
                time.sleep(0.1)
        return False

    def current_url(self):
        return self.browser.current_url

    def click(self, xpath: str):
        self.browser.find_element_by_xpath(xpath).click()

    def input(self, xpath: str, text: str):
        self.browser.find_element_by_xpath(xpath).send_keys(text)

    def clear(self, xpath: str):
        self.browser.find_element_by_xpath(xpath).clear()

    def back(self):
        self.browser.back()

    def text(self, xpath: str):
        return self.browser.find_element_by_xpath(xpath).text

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
        self.browser.find_element_by_xpath(xpath).submit()

    def exist(self, xpath: str, timeout: int = 3):
        now = time.time()
        while time.time() - now < timeout:
            try:
                self.browser.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return False
        return True

    def switch_to_title(self, title):
        self.browser.switch_to.window(title)

    def adblock_add_rule(self, rules=[]):
        if rules is None or len(rules) == 0:
            return
        self.open("chrome-extension://gighmmpiobklfepjocnamgkkbiglidom/options.html")
        # click custom
        self.wait_do('//*[@id="tabpages"]/ul/li[3]', self.click)
        # click edit
        self.wait_do('//*[@id="btnEditAdvancedFilters"]', self.click)
        self.wait('//*[@id="txtFiltersAdvanced"]')
        # click textarea
        textarea = self.browser.find_element_by_xpath('//*[@id="txtFiltersAdvanced"]')
        for rule in rules:
            textarea.send_keys(Keys.ENTER)
            textarea.send_keys(rule)
        # save
        time.sleep(.2)
        self.wait_do('//*[@id="btnSaveAdvancedFilters"]', self.click)
