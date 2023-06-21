from notes.vocabulary import Vocabulary


class Verb(Vocabulary):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__past = kwargs['past'] if 'past' in kwargs else ''
        self.__progressive = kwargs['progressive'] if 'progressive' in kwargs else ''

    @property
    def past(self) -> str:
        return self.__past

    @past.setter
    def past(self, past: str) -> None:
        self.__past = past

    @property
    def progressive(self) -> str:
        return self.__progressive

    @progressive.setter
    def progressive(self, progressive: str) -> None:
        self.__progressive = progressive

    def __str__(self) -> str:
        return f'Verb(' \
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
               f'past={self.__past}, ' \
               f'progressive={self.__progressive})'
