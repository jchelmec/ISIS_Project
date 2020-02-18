import openData
from pathlib import Path



filename = '001-B1.txt'
data_obj = openData.LoadData()
data_obj.load_from_file(filename)
data_obj.detect_hummer_data(channel=2, sens=0.3 , len_imp=2, pre=0.2, post=3.8, plot = False)
data_obj.save_to_file()




# def is_pair(x):
#     return x % 2 == 0
#
# xs= ([1,2,3,4])
#
# wyn = [x
#        for x in xs
#        if is_pair(x)]
#
# print (wyn)

