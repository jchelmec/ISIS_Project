import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import hilbert
import numpy as np
from pathlib import Path
import threading


class LoadData:
    def __init__(self):
        """"""


    def load_from_file(self, filename):
        """wczytanie pliku i usuniecie zdublowanych kolumn z czasem"""
        self.filename = filename
        print ('Wczytuje plik: ' + filename)
        dane = pd.read_csv(self.filename, sep='\t')
        kanaly=(range(2,len(dane.columns),2))
        dane.drop(dane.columns[kanaly] ,axis=1, inplace = True)
        self.fs = 1/(dane.iloc[1,0]-dane.iloc[0,0])
        self.dane = dane
        return dane

    def save_to_file(self):
        """Zapisywanie wykrytych wymuszeń do oddzielnych plików """
        i=1
        for wymusz in self.detect:
            print(wymusz)
            filename_obc = self.filename.rpartition('.')
            new_filename = str(filename_obc[0]) + '_' + str(i) + str(filename_obc[1] + str(filename_obc[2]))
            dane_wybrane = self.dane.iloc[int(wymusz[0]):int(wymusz[1]),:]
            print ('Zapisuje plik: ' + new_filename)
            try:
                pd.DataFrame.to_csv(dane_wybrane,('out/' + new_filename), sep='\t', index=False)
            except FileNotFoundError:
                p = Path('out/')
                p.mkdir(parents=True, exist_ok=True)
                pd.DataFrame.to_csv(dane_wybrane, ('out/' + new_filename), sep='\t', index=False)
            i+=1







    def setDane(self,dane):
        self.dane=dane

    def calcTimeMean(self):
        """Kalkulacja średnich w czasie z przebiegów czasowych - próbka po probce
            w celu wyznaczenia zastępczej odpowiedzi """

    def detect_hummer_data(self, channel, sens, len_imp, pre, post, plot):
        """wykrywanie i podzielenie danych z wielu uderzeń młotka modalnego w pojedyńcze wymuszenia o stałej długości"""
        do_analizy = self.dane.iloc[:,channel]
        signal_anal = hilbert(do_analizy)
        obwiednia = np.abs(signal_anal)
        max_obw = np.max(obwiednia)
        i=0
        detect_glob=[]

        for x in obwiednia:
            if x > max_obw * sens:
                # print( i, '  ' ,x, "  " , max_obw * sens)
                detect_glob.append(i)
            i+=1

        detect_ext=[]
        for uderz in detect_glob:
            if detect_ext == []:
                detect_ext.append(uderz)
            else:
                if uderz > detect_ext[-1] + self.fs*len_imp:
                    detect_ext.append(uderz)

        detect = []
        for ex in detect_ext:
            detect.append([ex-pre*self.fs,ex+post*self.fs])

        if plot == True:
            self.fig, self.ax = plt.subplots(figsize=(15, 5))
            linie = []
            label_chan = 'Kanał :%d' % channel
            linie.append(self.ax.plot(self.dane.iloc[:, 0], do_analizy, label='Sygnal'))
            linie.append(self.ax.plot(self.dane.iloc[:, 0], obwiednia, label='Obwiednia'))
            plt.title(label=self.filename)
            for ex in detect_ext:
                plt.axvspan(ex / self.fs - pre, ex / self.fs + post, facecolor='yellow', alpha=0.2)
            plt.setp(linie, linewidth=0.5)
            plt.show()


        # self.plot_thread = plotData(self.dane,channel, do_analizy, obwiednia,detect_ext,pre,post,self.filename, self.fs)
        # self.plot_thread.start()


        self.detect = detect
        return detect


    def plot_data(self,cols):
        """Wykresy czasowa wczytanych danych"""
        self.fig, self.ax = plt.subplots(figsize=(15, 5))
        linie = []

        linie.append(self.ax.plot(self.dane.iloc[:, 0], self.dane.iloc[:, 1:len(self.dane.columns)]))
        # linie.append(self.ax.plot(dane['ACC01_Time*'], dane['ACC07'], label='2'))

        plt.title(label=self.filename)
        plt.setp(linie, linewidth=0.5)
        przed = self.ax.get_xlim()

        zakres = (przed[1] - przed[0])
        self.napis_zakres = plt.figtext(0.9, 0.9, s='{:.2f}'.format(zakres), horizontalalignment='right')
        self.plt = plt
        cid = self.fig.canvas.mpl_connect('button_release_event', self.on_release)

    def on_release(self,event):
        przed =self.ax.get_xlim()

        zakres = (przed[1] - przed[0])
        self.napis_zakres.remove()
        # napis_zakres.remove()
        self.napis_zakres = plt.figtext(0.9, 0.9, s='{:.2f}'.format(zakres), horizontalalignment='right')
        print(self.napis_zakres)

