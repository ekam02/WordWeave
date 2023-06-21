from selenium.webdriver.common.by import By


class Ingles:
    MAIN = (By.ID, 'dictionary-neodict-en')  # Identifica la sección donde está la información principal
    CARDS = (By.CLASS_NAME, 'k5rFFEq7')  # Identifica los elementos o tarjetas a crear, lo uso para saber el número de
                                         # iteracciones
    CARD_TYPE = (By.CSS_SELECTOR, 'div>a.hWzdmlHx')  # Para cada elemento, se obtiene el tipo de tarjeta
    CARD_INFO = (By.CSS_SELECTOR, 'div.AJ6Kb8A8>div.lbHJ7w6W')  # Obtiene una lista con las piezas de traducción de cada tarjeta
    CARD_INFO_SUMMARY = (By.CLASS_NAME, 'UlJJEaZY')  # Para una pieza, obtiene el resumen
    CARD_INFO_TRANS = (By.CSS_SELECTOR, 'div.RiMg1_4r>div.lbHJ7w6W>div>span>a.YR6epHeU')
    # Para una pieza, trae una lista de traducciones

    # span.UlJJEaZY  # resumen
    # div.RiMg1_4r > div.lbHJ7w6W > div > span.YR6epHeU  # traducción
    # div.RiMg1_4r > div.lbHJ7w6W > div > div.QkSyASiy > div.lbHJ7w6W > span.S7halQ2C  # Ejemplo

    def __init__(self, driver):
        self.driver = driver

    def translation(self) -> str:
        driver.get(Config.INGLES.format('cut'))
        cards = driver.find_element(*Ingles.MAIN).find_elements(*Ingles.CARDS)
        for card in cards:
            lista_de_elementos = []
            card_info = card.find_elements(*Ingles.CARD_INFO)
            for slic in card_info:
                summary = slic.find_element(*Ingles.CARD_INFO_SUMMARY).text
                summary = f"<small>{summary.replace('(', '[').replace(')', ']')}</small>"
                translate = ', '.join([s.text for s in slic.find_elements(*Ingles.CARD_INFO_TRANS)])
                translate = ' '.join((summary, translate))
                lista_de_elementos.append(translate)
            print(', '.join(lista_de_elementos))