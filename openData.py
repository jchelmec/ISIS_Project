import pandas as pd
import matplotlib.pyplot as plt


class LoadData:
    def __init__(self,filename):
        self.filename = filename

    def load(self):
        dane = pd.read_csv(self.filename, sep='\t')
        kanaly=(range(2,len(dane.columns),2))
        dane.drop(dane.columns[kanaly] ,axis=1, inplace = True)
        print(dane.columns)
        return dane


class DataFragment:
    def __init__(self):
        plik = LoadData('001-B1.txt')
        dane = plik.load()

        # print (dane.iloc[:,0:6])
        self.fig,self.ax = plt.subplots(figsize=(15,5))
        linie=[]

        linie.append(self.ax.plot(dane['ACC01_Time*'],dane['ACC01'], label='1'))
        # linie.append(self.ax.plot(dane['ACC01_Time*'], dane['ACC07'], label='2'))

        plt.title(label = 'Macedonia')
        plt.setp(linie, linewidth = 0.5)
        przed = self.ax.get_xlim()


        zakres = (przed[1] - przed[0])
        self.napis_zakres = plt.figtext(0.9, 0.9, s='{:.2f}'.format(zakres), horizontalalignment='right')
        self.plt=plt
        cid = self.fig.canvas.mpl_connect('button_release_event',self.on_release)
        self.plt.legend()
        self.plt.show()

    def on_release(self,event):
        przed =self.ax.get_xlim()

        zakres = (przed[1] - przed[0])
        self.napis_zakres.remove()
        # napis_zakres.remove()
        self.napis_zakres = plt.figtext(0.9, 0.9, s='{:.2f}'.format(zakres), horizontalalignment='right')


        print(self.napis_zakres)




