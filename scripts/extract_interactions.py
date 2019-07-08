import os
import json
import random
import csv
import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

file_loc = '../../mprobc_250kb.txt'

with open(file_loc) as input_:
    stripped = [line.strip() for line in input_]
    lines = [s.split('\t')[1:] for s in stripped if s]

header = []
final_list=[]

for counter,line in enumerate(lines[1:]):
    abc = line[0]
    header.append(abc)
    new_list = [abc] + [int(math.fabs(math.floor(float(x)))) for x in line[1:]]
    final_list.append(new_list)


with open('../../mprobc_250kb.csv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter=',')
    for i in final_list:
        tsv_writer.writerow(i)

df = pd.read_csv('../../mprobc_250kb.csv',delimiter=',',header=None,index_col=None)
header = df.pop(0)

scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df)
df.loc[:,:] = scaled_values

frequency_threshold = 0.050

thres_inter_tar = []
thres_inter_sou = []
frequency = []
for chr_loc, i in enumerate(df.iterrows()):

    list_ = list(i[1])
#     print(i[1])
    for counter,j in enumerate(list_):
        if j >= frequency_threshold:
#             print(j)
            if header[counter] == header[chr_loc]:
                continue
            else:
                thres_inter_tar.append(header[counter])
                frequency.append(j)
                thres_inter_sou.append(header[chr_loc])
        else:
            continue

df_write = pd.DataFrame({
    'source':thres_inter_tar,
    'target':thres_inter_sou,
    'weight':frequency,
})

df_write.to_csv('interactions.csv',index=False)
