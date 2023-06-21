from notes.adjective import *
from notes.noun import *
from notes.verb import *
from notes.vocabulary import *


class Config:
    CAMBRIDGE = 'https://dictionary.cambridge.org/us/dictionary/english-spanish/{}'
    OXFORD = 'https://www.oxfordlearnersdictionaries.com/definition/english/{}'
    INGLES = 'https://www.ingles.com/traductor/{}?langFrom=en'
    TIME_OUT = 2
    BRAVE = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    WORDS = 'words.csv'
    TRANSLATER = {
        'ADJETIVO': Adjective,
        'ADVERBIO': Vocabulary,
        'ARTÍCULO DEFINIDO': Vocabulary,
        'CONJUNCIÓN': Vocabulary,
        'INTERJECCIÓN': Vocabulary,
        'PREPOSICIÓN': Vocabulary,
        'PRONOMBRE': Vocabulary,
        'SUSTANTIVO': Noun,
        'VERBO AUXILIAR': Verb,
        'VERBO COPULATIVO': Verb,
        'VERBO IMPERSONAL': Verb,
        'VERBO INTRANSITIVO': Verb,
        'VERBO TRANSITIVO': Verb
    }
