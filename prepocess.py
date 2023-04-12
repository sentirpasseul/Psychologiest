import math
import re


class Preprocess:

    def prepSent(self, text: list):
        self.text = text
        self.text_prep = list()
        for sent in self.text:
            if str(sent) == "nan":
                pass
            else:
                sent = re.sub("[,@\'?\.$%_]", "", sent)
                sent.lower()
                self.text_prep.append(sent)
        return self.text_prep


