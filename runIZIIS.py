import openData
import pandas as pd
from pathlib import Path

file = openData.fileDir('*.txt')

for x in file:
    # filename = '001-B1.dat'
    # data_obj = openData.LoadData()
    # data_obj.load_from_file(str(x))
    # data_obj.detect_hummer_data(channel=4, sens=0.3 , len_imp=2, pre=0.2, post=3.8, plot = True)
    # data_obj.save_to_file()

    # file = '001-B1.dat'
    f = openData.Wypadkowa(str(x))

    # Wybieranie kanałów do analizy
    # kan = [0, 1, 2, 3, 4, 5, 6]
    # dane_wybrane = f.wyborKanalow(kan)

            # print('------------------------------')
            # print('Dane wybrane')
            # print('------------------------------')
            # print(dane_wybrane)

    # skalowanie kanałów przez mnożnik, kanały w formie list lub taple
    for i in range(1, 16):
        f.skalowanieKanalow(i, 981)  # mnożnik do skalowania plików

    # dane_wyskalowane = f.getData()

    # print('------------------------------')
    # print('Dane wyskalowane')
    # print('------------------------------')
    # print(dane_wyskalowane)

    t = f.getData().iloc[:, 0]
    kan_wypad = [2,3]
    s1 = f.wypadkowaKanalow(kan_wypad)
    kan_wypad = [4,5]
    s2 = f.wypadkowaKanalow(kan_wypad)
    kan_wypad = [6,7,8,9]
    s3 = f.wypadkowaKanalow(kan_wypad)
    kan_wypad = [11,12,13,14]
    s4 = f.wypadkowaKanalow(kan_wypad)
    force = f.getData().iloc[:,30]

    # Składanie danych policzeniu wypadkowych z kontretnych kanałów.
    # Im więcej grup składowych tym więcej parametrów s
    dane_wypadkowe = pd.concat([t, s1, s2, s3, s4, force], axis=1)

    print('------------------------------')
    print('Dane wypadkowe')
    print('------------------------------')
    print(dane_wypadkowe)

    f.save_to_file(dane_wypadkowe)
