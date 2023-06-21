from selenium.webdriver.common.by import By
from selenium import webdriver
from utils.config import Config
from webdriver_manager.chrome import ChromeDriverManager


class Cambridge:
    SEARCH_INPUT = (By.NAME, 'q')
    HEADER = (By.CLASS_NAME, 'pos-header')
    IPA = (By.CLASS_NAME, 'ipa')

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def find_afi(self) -> list:
        afi = []

        def sup(string: str) -> str:
            return string.replace('<span class="sp dsp">', '<sup>').replace('</span>', '</sup>')

        for i in self.driver.find_element(*self.HEADER).find_elements(*self.IPA):
            afi.append('/' + sup(i.get_attribute('innerHTML')) + '/')

        limit = int(len(afi) / 2)
        return [afi[:limit], afi[limit:]]


if __name__ == '__main__':
    pass
    # brave = webdriver.ChromeOptions()
    # brave.binary_location = Config.BRAVE
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=brave)
    # driver.maximize_window()
    # home_page = Cambridge(driver)
    # driver.get(Config.CAMBRIDGE.format('translator'))
    # print(home_page.find_afi())
    # driver.close()
