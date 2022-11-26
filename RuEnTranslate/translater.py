from bob import RU_SYMBOLS, EN_SYMBOLS


class RuEnTranslater:
    def __init__(self, text: str):
        self.text = text

        self.ru_symbols = RU_SYMBOLS
        self.en_symbols = EN_SYMBOLS

        self._translate()

    def _translate(self) -> str:
        """Translate the en text to ru text
        :return: translated text"""

        self.correct_text = str()
        for letter in self.text:
            for index, symbol in enumerate(self.en_symbols):
                if letter == symbol:
                    self.correct_text += self.ru_symbols[index]

    def __str__(self) -> str:
        return self.correct_text


str_ = 'ghbdtn lhe;t'
print(RuEnTranslater(str_))
