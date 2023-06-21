import unittest

from utils.config import Config
from pages.cambridge import Cambridge
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class TestCambridge(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.brave = webdriver.ChromeOptions()
        cls.brave.binary_location = Config.BRAVE
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=cls.brave)
        cls.driver.maximize_window()
        cls.home_page = Cambridge(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    def test_home_page(self) -> None:
        self.driver.get(Config.CAMBRIDGE.format('cut'))
        ipa = self.home_page.find_afi()
        print(ipa)
        assert isinstance(ipa, list)

    def test_search_word(self):
        pass

    def test_find_afi(self):
        pass


if __name__ == '__main__':
    unittest.main()
