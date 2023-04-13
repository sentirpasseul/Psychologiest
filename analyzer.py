from morph import MorphAnalyzer


class Analyzer:

    def __init__(self):
       self.m_anlzr = MorphAnalyzer()

    def getMorphParse(self, text_morph: list):
        self.text_morph = text_morph

    def getInterj(self, text_morph: list):
        text_morph = self.m_anlzr.getMorphText(text_morph)
        interj_list = list()
        #print(len(text_morph))
        for sentence in text_morph:
            sentence = sentence.split()
            sentence = str(sentence[0].split(",")[0])
            #print(sentence)
            if sentence == 'МЕЖД':
                #print(f"В '{sentence}' есть междометие, записывается 1")
                interj_list.append(1)
            else:
                #print(f"В '{sentence}' нет междометия, записывается 0")
                interj_list.append(0)

        #print(len(interj_list))
        return interj_list


a1 = Analyzer()
#a1.getInterj(['МС,1л ед,им', 'ГЛ,несов,перех ед,1л,наст,изъяв', 'МС,2л ед,вн', 'Н,указ', 'ГЛ,несов,неперех,безл ед,наст,изъяв', 'СУЩ,неод,ср ед,им'])
#a1.getInterj(['там хорошо', 'я ряженку лучше люблю.', 'особенно когда придет комиссия проверять документацию', 'ды щаз приветик'])
