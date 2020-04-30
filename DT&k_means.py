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
    dataset.append(item)

label=[]
for i in range(len(dataset)):
    if dataset[i][0]=="0":
        train_num=i
        break
    label.append(int(dataset[i][0]))

for i in range(len(dataset)):
    dataset[i].pop(0)

for i in range(len(dataset)):
    for j in range(len(dataset[0])):
        dataset[i][j]=dataset[i][j].split(":")
        dataset[i][j][0]=int(dataset[i][j][0])
        dataset[i][j][1] = float(dataset[i][j][1])

train_data=dataset[0:train_num]
test_data=dataset[train_num:]

label_seq=list(set(label))
art_num=len(train_data[0])


###Decesion Tree###
def count_info(label_index):
    dem=sum(label_index)
    info_d=0
    for i in range(len(label_index)):
        if label_index[i]!=0:
            info_d=info_d-label_index[i]/dem*math.log(label_index[i]/dem,2)
    return info_d

def count_gini(label_num):
    dem=sum(label_num)
    if dem==0:
        gini=1
    else:
        gini=1
        for i in range(len(label_num)):
         gini=gini-pow(label_num[i]/dem,2)
    return gini


def count_label_num(list_tmp):
    count_num=[0]*len(label_seq)
    for i in range(len(list_tmp)):
        for j in range(len(label_seq)):
            if list_tmp[i]==label_seq[j]:
                count_num[j]=count_num[j]+1
    return count_num


def find_arb(data,label1):
    value_total_list = []
    for i in range(art_num):
        value_list = []
        for j in range(len(data)):
            value_list.append(data[j][i][1])
        value_total_list.append(value_list)
    total_label = count_label_num(label1)
    theta_list = []
    gini_list = []
    for i in range(art_num):
        count_label_art=[]
        list_ordered = sorted(list(enumerate(value_total_list[i])), key=lambda x: x[1])
        info_list=[]
        for j in range(len(data)):#split
            label_left_total=list_ordered[0:j+1]
            label_left=[]
            for k in range(len(label_left_total)):
                label_left.append(label1[label_left_total[k][0]])
            count_label_left=count_label_num(label_left)
            count_label_right=[]
            for k in range(len(count_label_left)):
                count_label_right.append(total_label[k]-count_label_left[k])
            info_list.append(sum(count_label_left)/len(data)*count_info(count_label_left)
                             +sum(count_label_right)/len(data)*count_info(count_label_right))
        min_sp=info_list.index(min(info_list))
        theta=(list_ordered[min_sp][1]+list_ordered[min_sp+1][1])/2
        theta_list.append(theta)
        left_node=[]
        for z in range(len(data)):
            if data[z][i][1]<theta:
                left_node.append(label1[z])
        count_node_left = count_label_num(left_node)
        count_node_right = []
        for k in range(len(count_node_left)):
            count_node_right.append(total_label[k] - count_node_left[k])
        gini_a=len(left_node)/len(data)*count_gini(count_node_left)+(1-(len(left_node)/len(data)))*count_gini(count_node_right)
        gini_list.append(gini_a)
    return theta_list,gini_list

theta_list1,gini_list1=find_arb(train_data,label)

split1=gini_list1.index(min(gini_list1))
left_nodes=[]
left_label=[]
right_nodes=[]
right_label=[]
for i in range(train_num):
    if train_data[i][split1][1]<theta_list1[split1]:
        left_nodes.append(train_data[i])
        left_label.append(label[i])
    else:
        right_nodes.append(train_data[i])
        right_label.append(label[i])
#print(right_nodes,"rightnodes")
#for left nodes
theta_list11,gini_list11=find_arb(left_nodes,left_label)

split11=gini_list11.index(min(gini_list11))
left_nodes1=[]
left_label1=[]
right_nodes1=[]
right_label1=[]
for i in range(len(left_nodes)):
    if left_nodes[i][split11][1]<theta_list11[split11]:
        left_nodes1.append(left_nodes[i])
        left_label1.append(left_label[i])
    else:
        right_nodes1.append(left_nodes[i])
        right_label1.append(left_label[i])
label_a=Counter(left_label1)
if len(label_a)!=0:
    label_a=label_a.most_common(1)
    label_a=int(label_a[0][0])
label_b=Counter(right_label1)
if len(label_b)!=0:
    label_b=label_b.most_common(1)
    label_b=int(label_b[0][0])
#for right nodes
#print("rl",right_label)
theta_list12,gini_list12=find_arb(right_nodes,right_label)
#print("gini12",gini_list12)
#print("theta12",theta_list12)
split12=gini_list12.index(min(gini_list12))
#print("sl",split12)
left_nodes2=[]
left_label2=[]
right_nodes2=[]
right_label2=[]
for i in range(len(right_nodes)):
    if right_nodes[i][split12][1]<theta_list12[split12]:
        left_nodes2.append(right_nodes[i])
        left_label2.append(right_label[i])
    else:
        right_nodes2.append(right_nodes[i])
        right_label2.append(right_label[i])
label_c=Counter(left_label2)
if len(label_c)!=0:
    label_c=label_c.most_common(1)
    label_c=int(label_c[0][0])
label_d=Counter(right_label2)
if len(label_d)!=0:
    label_d=label_d.most_common(1)
    label_d=int(label_d[0][0])
#print("c",label_c)
#print("d",label_d)
#test data
test_label_dt=[]
for i in range(len(test_data)):
    if test_data[i][split1][1]<=theta_list1[split1]:
        if test_data[i][split11][1]<=theta_list11[split11]:
            test_label_dt.append(label_a)
        else:
            test_label_dt.append(label_b)
    else:
        if test_data[i][split12][1]<=theta_list12[split12]:
            test_label_dt.append(label_c)
        else:
            test_label_dt.append(label_d)

##KNN##
n=len(label_seq)
def knn(test_point):
    dist = []
    for j in range(len(train_data)):
        d=0
        for k in range(len(train_data[0])):
            d=d+pow((train_data[j][k][1]-test_point[k][1]),2)
        dist.append(d)
    min_index_list = list(map(dist.index, heapq.nsmallest(3, dist)))
    label_target=[]
    for i in min_index_list:
        label_target.append(int(label[i]))
    if len(set(label_target))==3:
        target=min(label_target)
    else:
        counts=Counter(label_target)
        target=counts.most_common(1)
        target=int(target[0][0])
    return target

knn_label=[]
for l in range(len(test_data)):
    knn_label_l=knn(test_data[l])
    knn_label.append(knn_label_l)


for i in range(len(test_label_dt)):
    print(test_label_dt[i])
print("")
for i in range(len(knn_label)):
    print(knn_label[i])