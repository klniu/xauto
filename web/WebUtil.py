from selenium import webdriver


class WebUtil:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def open(self, url: str):
        self.browser.get(url)

    def input(self, xpath: str, text: str):
        with WaitForPageLoad(self.browser):
            self.browser.find_element_by_xpath(xpath).send_keys(text)

    def close(self):
        self.browser.close()


class WaitForPageLoad(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def __exit__(self, *_):
        self.wait_for(self.page_has_loaded)

    def wait_for(self, condition_function):
        import time

        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for {}'.format(condition_function.__name__)
        )

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id



