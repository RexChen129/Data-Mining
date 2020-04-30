import sys
import collections
##input dataset##
dataset=[]
while True:
    line = sys.stdin.readline().strip()
    if line=='':
        break
    item = line.split(' ')
    dataset.append(item)
tra_num=dataset.__len__()

count2=[]
for i in range(tra_num):
    for j in range(len(dataset[i])-1):
        count2.append(dataset[i][j]+" "+dataset[i][j+1])
frequency2 = collections.Counter(count2)
frequency2 = {k:v for k,v in frequency2.items() if v >= 2}

count3=[]
for i in range(tra_num):
    for j in range(len(dataset[i])-2):
        count3.append(dataset[i][j]+" "+dataset[i][j+1]+" "+dataset[i][j+2])
frequency3 = collections.Counter(count3)
frequency3 = {k:v for k,v in frequency3.items() if v >= 2}

count4=[]
for i in range(tra_num):
    for j in range(len(dataset[i])-3):
        count4.append(dataset[i][j]+" "+dataset[i][j+1]+" "+dataset[i][j+2]+" "+dataset[i][j+3])
frequency4 = collections.Counter(count4)
frequency4 = {k:v for k,v in frequency4.items() if v >= 2}

count5=[]
for i in range(tra_num):
    for j in range(len(dataset[i])-4):
        count5.append(dataset[i][j]+" "+dataset[i][j+1]+" "+dataset[i][j+2]+" "+dataset[i][j+3]+" "+dataset[i][j+4])
frequency5 = collections.Counter(count5)
frequency5 = {k:v for k,v in frequency5.items() if v >= 2}
fp={}
fp.update(frequency2)
fp.update(frequency3)
fp.update(frequency4)
fp.update(frequency5)
f_num=list(set(list(fp.values())))
f_num=sorted(f_num,reverse=True)
sort_fp=sorted(fp.items(),key=lambda item:(-item[1],item[0]))
sort_fp=sort_fp[:20]
for i in range(len(sort_fp)):
    print("[", sort_fp[i][1], ",", " ", "'", sort_fp[i][0], "'", "]", sep="")


