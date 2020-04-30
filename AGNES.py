import sys
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
train_data=dataset[1:]
dimension=len(train_data[0])
dist_list=[]

def count_dist(x,y):
    return sum([(x[i] - y[i])**2 for i in range(len(x))])

for i in train_data:
    dist=[]
    for j in train_data:
        dist.append(count_dist(i,j))
    dist_list.append(dist)


def count_cluster_dist(c1,c2):
    dist_cluster=[]
    for i in c1:
        for j in c2:
            dist_cluster.append(dist_list[i][j])
    return min(dist_cluster)

def update_id(cluster_id_tmp):
    cls_d=[]
    l=len(cluster_id_tmp)
    for i in range(l):
        cd=[]
        for j in range(i):
            if i!=j:
                cd.append(count_cluster_dist(cluster_id_tmp[i],cluster_id_tmp[j]))
        cls_d.append(cd)
    cls_d[0].append(99999)
    a=min(min(row) for row in cls_d)
    for i in range(len(cls_d)):
        if a in cls_d[i]:
            id1=i
            id2=cls_d[i].index(a)
            break
    cluster_id_tmp[id1]=cluster_id_tmp[id1]+cluster_id_tmp[id2]
    cluster_id_tmp.pop(id2)
    return cluster_id_tmp

cluster_id=[]
for i in range(train_num):
    cluster_id.append([i])

while len(cluster_id)>k:
    cluster_id=update_id(cluster_id)

k_list=[]
for i in range(k):
    k_list.append(min(cluster_id[i]))
for i in range(train_num):
    for j in range(k):
        if i in cluster_id[j]:
            print(k_list[j])
            break
