import pymorphy2

morph = pymorphy2.MorphAnalyzer()

class MorphAnalyzer:


    def getMorphSent(self, text: list):
        self.text = text
        self.text_morph = list()
        for sentence in self.text:
            sentence = sentence.split()
            for word in sentence:
                if word == " ":
                    pass
                else:
                    parts = morph.parse(word)[0]
                    part = parts.tag.cyr_repr
                    self.text_morph.append(parts)

        return self.text_morph

m1 = MorphAnalyzer().getMorphSent(['Я люблю тебя', "Там стоит дерево"])
print(m1)