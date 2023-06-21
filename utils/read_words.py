from utils.config import Config


class ReadWords:
    def __init__(self, file=Config.WORDS) -> None:
        with open(file) as words:
            self.words = [line.replace('\n', '') for line in words]
        words.close()

    def get_words(self) -> list:
        return self.words


if __name__ == '__main__':
    a = ReadWords().get_words()
    print(a)
