import unittest
from selenium import webdriver
from pages.oxford import Oxford
from utils.config import Config
from webdriver_manager.chrome import ChromeDriverManager


class TestOxford(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome_options = webdriver.ChromeOptions()
        cls.chrome_options.binary_location = Config.BRAVE
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=cls.chrome_options)
        cls.driver.maximize_window()
        cls.home_page = Oxford(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    def test_find_data_src_mp3(self) -> None:
        self.driver.get(Config.OXFORD.format('translator'))
        assert isinstance(self.home_page.find_data_src_mp3(), list)
