import math
import re


class Preprocess:

    def prepSent(self, text: list):
        self.text = text
        self.text_prep = list()
        for sent in self.text:
            if str(sent) == "nan":
                self.text_prep.append("0")
            else:
                sent = sent.split()
                sent = " ".join(sent)
                sent = re.sub("[,@\'?\.$%_]", "", sent)
                sent.lower()
                self.text_prep.append(sent)
        #print(self.text_prep)
        return self.text_prep


#p1 = Preprocess().prepSent([' I love'])