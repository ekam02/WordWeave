from notes.vocabulary import Vocabulary


class Adjective(Vocabulary):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__comparative = kwargs['comparative'] if 'comparative' in kwargs else ''
        self.__superlative = kwargs['superlative'] if 'superlative' in kwargs else ''
        self.__adverb = kwargs['adverb'] if 'adverb' in kwargs else ''

    @property
    def comparative(self) -> str:
        return self.__comparative
    
    @comparative.setter
    def comparative(self, comparative: str) -> None:
        self.__comparative = comparative
    
    @property
    def superlative(self) -> str:
        return self.__superlative
    
    @superlative.setter
    def superlative(self, superlative: str) -> None:
        self.__superlative = superlative
    
    @property
    def adverb(self) -> str:
        return self.__adverb
    
    @adverb.setter
    def adverb(self, adverb: str) -> None:
        self.__adverb = adverb

    def __str__(self) -> str:
        return f'Adjective(' \
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
               f'comparative={self.__comparative}, '\
               f'superlative={self.__superlative}, '\
               f'adverb={self.__adverb})'
