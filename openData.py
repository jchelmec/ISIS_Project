import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import hilbert
import numpy as np



class LoadData:
    def __init__(self,filename):
        self.filename = filename

    def load_from_file(self):
        """wczytanie pliku i usuniecie zdublowanych kolumn z czasem"""
        dane = pd.read_csv(self.filename, sep='\t')
        kanaly=(range(2,len(dane.columns),2))
        dane.drop(dane.columns[kanaly] ,axis=1, inplace = True)
        self.dane = dane
        return dane

    def setDane(self,dane):
        self.dane=dane

    def calcTimeMean(self):
        """Kalkulacja średnich w czasie z przebiegów czasowych - próbka po probce
            w celu wyznaczenia zastępczej odpowiedzi """

    def detect_hummer_data(self, channel):
        """wykrywanie i podzielenie danych z wielu uderzeń młotka modalnego w pojedyńcze wymuszenia o stałej długości"""
        do_analizy = self.dane.iloc[:,channel]
        signal_anal = hilbert(do_analizy)
        obwiednia = np.abs(signal_anal)
        max_obw = np.max(obwiednia)
        i=0
        detect=[]

        for x in obwiednia:
            if x > max_obw*0.5:
                print( i, '  ' ,x, "  " , max_obw * 0.5)
                detect.append([self.dane.iloc[i,0],x])
            i+=1
        print(detect)

        self.fig, self.ax = plt.subplots(figsize=(15, 5))
        linie = []
        label_chan= 'Kanał :%d' % channel
        linie.append(self.ax.plot(self.dane.iloc[:,0], do_analizy, label='Sygnal' ))
        linie.append(self.ax.plot(self.dane.iloc[:,0], obwiednia, label='Obwiednia'))
        plt.title(label=self.filename)
        plt.setp(linie, linewidth=0.5)
        plt.show()

    def plot_data(self,cols):
        """Wykresy czasowa wczytanych danych"""

class DataFragment:

    def __init__(self):
        filename = '001-B1.txt'
        obj_dane = LoadData(filename)
        dane = obj_dane.load_from_file()

        # print (dane.iloc[:,0:6])
        self.fig,self.ax = plt.subplots(figsize=(15,5))
        linie=[]

        linie.append(self.ax.plot(dane.iloc[:,0],dane.iloc[:,1:len(dane.columns)]))
        # linie.append(self.ax.plot(dane['ACC01_Time*'], dane['ACC07'], label='2'))

        plt.title(label = filename)
        plt.setp(linie, linewidth = 0.5)
        przed = self.ax.get_xlim()


        zakres = (przed[1] - przed[0])
        self.napis_zakres = plt.figtext(0.9, 0.9, s='{:.2f}'.format(zakres), horizontalalignment='right')
        self.plt=plt
        cid = self.fig.canvas.mpl_connect('button_release_event',self.on_release)
        # self.plt.legend()
        # self.plt.show()

        obj_dane.detect_hummer_data(channel=1)

    def on_release(self,event):
        przed =self.ax.get_xlim()

        zakres = (przed[1] - przed[0])
        self.napis_zakres.remove()
        # napis_zakres.remove()
        self.napis_zakres = plt.figtext(0.9, 0.9, s='{:.2f}'.format(zakres), horizontalalignment='right')


        print(self.napis_zakres)




