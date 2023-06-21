from selenium.webdriver.common.by import By
from selenium import webdriver
from utils.config import Config
from webdriver_manager.chrome import ChromeDriverManager


class Oxford:
    # reconocer todos elementos que guardan url de los sonidos
    SOUND = (By.CSS_SELECTOR, 'div.sound')
    DATA_SRC_MP3 = 'data-src-mp3'
    # De estos se escoge el atributo con nombre "data-src-mp3"
    # Para filtrar lo que queremos se puede recorrer la lista de elementos y solo sacar el atributo "data-src-mp3"

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def find_data_src_mp3(self) -> list:
        sounds = self.driver.find_elements(*Oxford.SOUND)
        return [data_src_mp3.get_attribute(Oxford.DATA_SRC_MP3) for data_src_mp3 in sounds]


if __name__ == '__main__':
    pass
    # brave = webdriver.ChromeOptions()
    # brave.binary_location = Config.BRAVE
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=brave)
    # driver.maximize_window()
    # driver.get('https://www.oxfordlearnersdictionaries.com/definition/english/{}'.format('translator'))
    # sounds = driver.find_elements(*Oxford.SOUND)
    # print([data_src_mp3.get_attribute(Oxford.DATA_SRC_MP3) for data_src_mp3 in sounds])
    # driver.close()
