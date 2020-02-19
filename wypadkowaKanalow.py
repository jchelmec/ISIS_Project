import pandas as pd


class Wypadkowa:
    def __init__(self, filename):
        self.filename = filename

    def wyborKanalow(self, kanaly):
        """Odczyt wybranych kanałów"""
        self.dane = pd.read_csv(self.filename, sep='\t', usecols=kanaly)
        print(self.dane.iloc[0:10,:])
        return self.dane

    def wypadkowaKanalow(self,kanaly):
        """Obliczanie wypadkowej wybranych kanałów kanalów"""

        print(self.dane.pop(self.dane.columns[kanaly]))
        # dane_wyp = self.dane.pop(self.dane.columns[kanaly])
        # print(dane_wyp.iloc[0:10])
        # print(self.dane.iloc[0:10,:])

    def skalowanieKanalow(self, kanal):
        """Skalowanie kanałów"""


filename='dane_testowe.txt'
f = Wypadkowa(filename)

# kan = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,31]
# kan =[]
# for x in range(1,17): kan.append(x)
# kan.append(31)

kan = [0,1,2,3,4,5,6]
print(kan)
f.wyborKanalow(kan)
kan_wypad = [1,2,3,4]
f.wypadkowaKanalow(kan_wypad)

