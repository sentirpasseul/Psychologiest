from matplotlib import pyplot as plt

class Draw:

    def drawDiag(self, array: list):
        plt.plot(array)
        plt.ylabel('Показатели')
        plt.show()


#d1 = Draw().drawDiag([1,2,3,4,5])