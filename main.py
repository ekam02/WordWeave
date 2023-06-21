from pages.ingles import Ingles
from selenium import webdriver
from utils.config import Config
from webdriver_manager.chrome import ChromeDriverManager


brave = webdriver.ChromeOptions()
brave.binary_location = Config.BRAVE
driver = webdriver.Chrome(ChromeDriverManager().install(), options=brave)
driver.maximize_window()
home_page = Ingles(driver)





driver.close()

# lista = []
# words = ReadWords('utils/words.csv')
#
# for k in words.get_words():
#     driver.get(Config.INGLES.format(k))
#     # if driver.find_element(*Ingles.MAIN) == 0:
#     #     continue
#     cards = driver.find_element(*Ingles.MAIN).find_elements(*Ingles.CARD_TYPE)
#     for i in cards:
#         card_type = i.text
#         if card_type not in lista:
#             lista.append(card_type)
#
