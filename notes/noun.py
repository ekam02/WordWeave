from notes.vocabulary import Vocabulary


class Noun(Vocabulary):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__plural = kwargs['plural'] if 'plural' in kwargs else ''

    @property
    def plural(self) -> str:
        return self.__plural

    @plural.setter
    def plural(self, plural: str) -> None:
        self.__plural = plural

    def __str__(self) -> str:
        return f'Noun(' \
               f'id={self.id}, ' \
               f'ask={self.ask}, ' \
               f'answer={self.answer}, ' \
               f'definition={self.definition}, ' \
               f'example={self.example}, ' \
               f'uk_afi={self.uk_afi}, ' \
               f'us_afi={self.us_afi}, ' \
               f'type={self.type}, ' \
               f'uk_sound={self.uk_sound}, ' \
               f'us_sound={self.us_sound}, ' \
               f'img={self.img}, ' \
               f'plural={self.__plural})'
