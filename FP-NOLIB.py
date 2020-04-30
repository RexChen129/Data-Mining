import sys
from itertools import combinations

##input dataset##
dataset=[]
print("Please input the transaction dataset, press Enter when finished.")
while True:
    line = sys.stdin.readline().strip()

    if line=='':
        break
    item = line.split(' ')
    dataset.append(item)
#print(dataset)

min_sup=list(map(eval,dataset[0]))
dataset.pop(0)
tra_num=dataset.__len__()
dict={ }
##1-itemset##
for i in range(tra_num):
    for j in dataset[i]:
        dict[j]=dict.get(j, 0) + 1
dict1 = {k:v for k,v in dict.items() if v >= min_sup[0]}
dict2=sorted(dict1.items(),key=lambda x:x[1],reverse=True)

##other iteration##
def count_num(k):
    dict_x = {}
    list_k = sorted(list(combinations(dict1.keys(), k)))
    c_num = list_k.__len__()
    str = ' '
    for i in range(c_num):
        for j in range(tra_num):
            if set(list_k[i]).issubset(dataset[j]):
                dict_x[str.join(list(sorted(list_k[i])))] = dict_x.get(str.join(sorted(list(list_k[i]))), 0) + 1
    dictx = {k: v for k, v in dict_x.items() if v >= min_sup[0]}
    dictx = sorted(dictx.items(), key=lambda x: x[1], reverse=True)
    return dictx

list_total=dict2
for i in range(1000):
    dict_tmp=count_num(i+2)
    if dict_tmp:
        list_total=list_total+dict_tmp
    else:
        break
list_sorted=sorted(list_total,key=lambda x:(-x[1],x[0]))

len_str=[]
##count closed&max pattern##
for i in range(len(list_sorted)):
    s=list_sorted[i][0].count(" ")+1
    len_str.append(s)
len_max=max(len_str)
list_closed=[]
loc=[i for i,x in enumerate(len_str) if x== len_max]
for i in loc:
    list_closed.append(list_sorted[i])
list_max=list_closed
def find_c(l):
    close_tmp=[]
    loc=[i for i,x in enumerate(len_str) if x== l]
    for i in loc:
        close_tmp.append(list_sorted[i])
    return close_tmp

while len_max!=0:
    close_tmp=find_c(len_max)
    max_tmp=find_c(len_max)
    list_closed1 = sorted(list_closed, key=lambda x: (-x[1], x[0]))
    max_close_sup=list_closed1[0][1]
    del_list=[]
    for i in range(len(close_tmp)):
        for j in range(len(list_closed)):

            try:
                str_set_tmp=list(close_tmp[i][0].split(" "))
                str_set_close=list(list_closed[j][0].split(" "))
                if set(str_set_tmp).issubset(set(str_set_close)):
                    if close_tmp[i][1]<=max_close_sup:
                        del_list.append(i)
            except:
                continue
    del_list=list(set(del_list))
    for i in sorted(del_list,reverse=True):
        del close_tmp[i]

    del_list = []
    for i in range(len(max_tmp)):
        for j in range(len(list_max)):
            str_set_tmp = list(max_tmp[i][0].split(" "))
            str_set_close = list(list_max[j][0].split(" "))
            try:
                if set(str_set_tmp).issubset(set(str_set_close)):
                     del_list.append(i)
            except:
                continue
    del_list = list(set(del_list))
    for i in sorted(del_list,reverse=True):
        del max_tmp[i]
    list_closed=list_closed+close_tmp
    list_max=list_max+max_tmp
    len_max=len_max-1

list_closed=sorted(list_closed,key=lambda x:(-x[1],x[0]))
list_max=sorted(list_max,key=lambda x:(-x[1],x[0]))


##print out#
file1 = sys.stdout
sys.stdout = open('1.txt',"w")
for i in range(len(list_sorted)):
    print(int(list_sorted[i][1])," ","[",str(list_sorted[i][0]),"]",sep="")
print("")
for i in range(len(list_closed)):
    print(int(list_closed[i][1])," ","[",str(list_closed[i][0]),"]",sep="")
print("")
for i in range(len(list_max)):
    print(int(list_max[i][1])," ","[",str(list_max[i][0]),"]",sep="")
sys.stdout.close()
sys.stdout = file1



