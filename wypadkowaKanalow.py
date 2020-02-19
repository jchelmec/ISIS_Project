import pandas as pd


class Wypadkowa:
    def __init__(self, filename):
        self.filename = filename
        self.dane = pd.read_csv(self.filename, sep='\t')


    def wyborKanalow(self, kanaly:int):
        """Odczyt wybranych kanałów"""
        self.dane =self.dane.filter(self.dane.iloc[:,kanaly])
        return self.dane

    def wypadkowaKanalow(self,kanaly:int):
        """Obliczanie wypadkowej wybranych kanałów kanalów"""

        dane_wyp = self.dane.iloc[:,kanaly[0]]
        for i in range(1,len(kanaly)):
            dane_wyp += self.dane.iloc[:,kanaly[i]]
        return dane_wyp / len(kanaly)

    def skalowanieKanalow(self, kanal:int, mnoznik:int):
        """Skalowanie kanałów"""
        self.dane.iloc[:,kanal] *= mnoznik
        return self.dane

    def getData(self):
        return self.dane

class PrepData:
    def __init__(self,filename):
        self.filename = filename


        f = Wypadkowa(filename)

        # dane_wejsciowe = f.getData()
        # print('-----------------------------')
        # print ('dane wejsciowe')
        # print('-----------------------------')
        # print(dane_wejsciowe)

        # kan = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,31]
        # kan =[]
        # for x in range(1,17): kan.append(x)
        # kan.append(31)

        kan = [0,1,2,3,4,5,6]

        dane_wybrane = f.wyborKanalow(kan)

        # print('------------------------------')
        # print('Dane wybrane')
        # print('------------------------------')
        # print(dane_wybrane)


        # f.wypadkowaKanalow(kan_wypad)
        for i in range (1,16):
            f.skalowanieKanalow(i,2)        # mnożnik do skalowania plików

        dane_wyskalowane = f.getData()

        # print('------------------------------')
        # print('Dane wyskalowane')
        # print('------------------------------')
        # print(dane_wyskalowane)

        t= f.getData().iloc[:,0]
        kan_wypad = [4,5,6]
        s1 = f.wypadkowaKanalow(kan_wypad)
        kan_wypad = [5,6]
        s2= f.wypadkowaKanalow(kan_wypad)
        kan_wypad = [6,10]
        s3 = f.wypadkowaKanalow(kan_wypad)

        self.dane_wypadkowe = pd.concat([t, s1, s2, s3], axis= 1 )

        print('------------------------------')
        print('Dane wypadkowe')
        print('------------------------------')
        print(self.dane_wypadkowe)

    def saveData(self):
        pd.

filename='dane_testowe.txt'

PrepData(filename)