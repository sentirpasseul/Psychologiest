import pymorphy2
import prepocess

morph = pymorphy2.MorphAnalyzer()

class MorphAnalyzer:


    def getMorphText(self, text: list):
        self.text = prepocess.Preprocess().prepSent(text)
        self.text_morph = list()
        sentence_morph = list()
        for sentence in self.text:
            #print(sentence)
            sentence = sentence.split()
            for word in sentence:
                if str(word) == " ":
                    pass
                else:
                    parts = morph.parse(word)[0]
                    part = parts.tag.cyr_repr
                    #print(f"Для слова '{word}': {part}") #log
                    sentence_morph.append(part)
            self.text_morph.append(part)

        return self.text_morph

#m1 = MorphAnalyzer().getMorphSent(['Я люблю тебя', "Там стоит дерево"])
#print(m1)