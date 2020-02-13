import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('001-B1.txt',sep='\t')
print (dane)

plt.plot(dane['ACC01_Time*'],dane['ACC03'])
print(dane.columns)
plt.show()