import sys
import heapq
from collections import Counter
import math
##input dataset##
dataset=[]
while True:
    line = sys.stdin.readline().strip()
    if line=='':
        break
    item = line.split(' ')
    for i in range(len(item)):
        item[i]=float(item[i])
    dataset.append(item)

train_num=int(dataset[0][0])
k=int(dataset[0][1])
train_data=dataset[1:train_num+1]
init=dataset[train_num+1:]
dimension=len(train_data[0])

def kmeans(init_point):
    dist_table=[]
    for i in range(len(train_data)):
        dist_list=[]
        for z in range(len(init_point)):
            dist=0
            for j in range(dimension):
                dist=dist+pow((train_data[i][j]-init_point[z][j]),2)
            dist_list.append(dist)
        dist_table.append(dist_list)
    k_list=[]
    for i in range(len(dist_table)):
        k_list.append(dist_table[i].index(min(dist_table[i])))
    return k_list

def update_center(k_list1):
    center_list=[]
    for i in range(k):
        center=[]
        for j in range(dimension):
            tmp=0
            for z in range(len(cluster_list[i])):
                tmp+=cluster_list[i][z][j]
            tmp=tmp/len(cluster_list[i])
            center.append(tmp)
        center_list.append(center)
    return center_list

k_list_tmp=kmeans(init)
for i in range(10):
    center_tmp=update_center(k_list_tmp)
    k_list_tmp=kmeans(center_tmp)

for i in range(train_num):
    print(k_list_tmp[i])