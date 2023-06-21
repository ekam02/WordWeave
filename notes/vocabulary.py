from utils.ident import Ident


class Vocabulary(Ident):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__id = kwargs['id'] if 'id' in kwargs else self.identifier()[0]
        self.__ask = kwargs['ask'] if 'ask' in kwargs else ''
        self.__answer = kwargs['answer'] if 'answer' in kwargs else ''
        self.__definition = kwargs['definition'] if 'definition' in kwargs else ''
        self.__example = kwargs['example'] if 'example' in kwargs else ''
        self.__uk_afi = kwargs['uk_afi'] if 'uk_afi' in kwargs else ''
        self.__us_afi = kwargs['us_afi'] if 'us_afi' in kwargs else ''
        self.__type = kwargs['type'] if 'type' in kwargs else ''
        self.__uk_sound = kwargs['uk_sound'] if 'uk_sound' in kwargs else ''
        self.__us_sound = kwargs['us_sound'] if 'us_sound' in kwargs else ''
        self.__img = kwargs['img'] if 'img' in kwargs else ''

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, identifier: str) -> None:
        self.__id = identifier if isinstance(identifier, str) else self.identifier()[0]

    @property
    def ask(self) -> str:
        return self.__ask

    @ask.setter
    def ask(self, ask: str) -> None:
        self.__ask = ask

    @property
    def answer(self) -> str:
        return self.__answer

    @answer.setter
    def answer(self, answer: str) -> None:
        self.__answer = answer

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str) -> None:
        self.__definition = definition

    @property
    def example(self) -> str:
        return self.__example

    @example.setter
    def example(self, example: str) -> None:
        self.__example = example

    @property
    def uk_afi(self) -> str:
        return self.__uk_afi

    @uk_afi.setter
    def uk_afi(self, uk_afi: str) -> None:
        self.__uk_afi = uk_afi

    @property
    def us_afi(self) -> str:
        return self.__us_afi

    @us_afi.setter
    def us_afi(self, us_afi: str) -> None:
        self.__us_afi = us_afi

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, _type: str) -> None:
        self.__type = _type

    @property
    def uk_sound(self) -> str:
        return self.__uk_sound

    @uk_sound.setter
    def uk_sound(self, uk_sound: str) -> None:
        self.__uk_sound = uk_sound

    @property
    def us_sound(self) -> str:
        return self.__us_sound

    @us_sound.setter
    def us_sound(self, us_sound: str) -> None:
        self.__us_sound = us_sound

    @property
    def img(self) -> str:
        return self.__img

    @img.setter
    def img(self, img: str) -> None:
        self.__img = img

    def __str__(self) -> str:
        return f'Vocabulary(' \
               f'id={self.__id}, ' \
               f'ask={self.__ask}, ' \
               f'answer={self.__answer}, ' \
               f'definition={self.__definition}, ' \
               f'example={self.__example}, ' \
               f'uk_afi={self.__uk_afi}, ' \
               f'us_afi={self.__us_afi}, ' \
               f'type={self.__type}, ' \
               f'uk_sound={self.__uk_sound}, ' \
               f'us_sound={self.__us_sound}, ' \
               f'img={self.__img})'
