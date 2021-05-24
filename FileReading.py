import csv
import pandas as pd
def csv_to_dict(file_name):
    d={}
    try:
        file = open(file_name,"r")
    except FileNotFoundError:
        print("FileNotFound")
    else:
        for line in file:
            line = line.strip('\n')
            (key,val)=line.split("\t")
            d[key] =val
            
    return d 


def txttoList (file_name, list_name):
    list_name =[]
    try:
        file=open('{}'.format(file_name),"r")     #以读模式打开文件
    except FileNotFoundError:          #如果文件不存在，给提示
        print("file is not found")
    else:
        contents=file.readlines()       #读取全部行
        for content in contents:       #显示一行
            list_name.append(content.split('\t')[0])
    
    return list_name
        # print(content.split('\t')[0])   #每行用逗号(这里是用Tab做分割）分隔后，取第一个元素

def dict2csv(dict,file):
    with open(file,'w') as f:
        w=csv.writer(f)
        # write all keys on one row and all values on the next
        w.writerow(dict.keys())
        w.writerow(dict.values())

def list_Intersection(list_1,list_2):
    A = set(list_1)
    B = set(list_2)
    return list (A & B)







wtTEVsorted =[]        
try:
    file=open('wtTEV-sorted_full.txt',"r")     #以读模式打开文件
except FileNotFoundError:          #如果文件不存在，给提示
    print("file is not found")
else:
    contents=file.readlines()       #读取全部行
    for content in contents:       #显示一行
       wtTEVsorted.append(content.split('\t')[0])
       # print(content.split('\t')[0])   #每行用逗号(这里是用Tab做分割）分隔后，取第一个元素

wtTEVnaive =[]        
try:
    file=open('wtTEV-naive_full.txt',"r")     #以读模式打开文件
except FileNotFoundError:          #如果文件不存在，给提示
    print("file is not found")
else:
    contents=file.readlines()       #读取全部行
    for content in contents:       #显示一行
       wtTEVnaive.append(content.split('\t')[0])
       # print(content.split('\t')[0])   #每行用逗号(这里是用Tab做分割）分隔后，取第一个元素




sorted = set(wtTEVsorted)
naive = set(wtTEVnaive)
tmp = sorted & naive
tmp2 = sorted - tmp #包含所有Sorted-（N&S）的set
tmp3 = naive - tmp #包含所有Naive-（N&S）的set


tmp2_list = list(tmp2)
tmp3_list = list(tmp3)

comp = []
comp_R = []

wtSorted_Dict = csv_to_dict('wtTEV-sorted_full.csv')
wtNaive_Dict = csv_to_dict('wtTEV-Naive_full.csv')

#FInding the dict for Sorted-(Sorted&Naive)
my_Dict ={}

for len in tmp2:
    my_Dict.update({len:wtSorted_Dict[len]})

    #my_Dict["Sequence"].append([len])
    #my_Dict["Counts"].append(wtSorted_Dict[len])

#finding the dict for Naive-(Sorted&Naive)
my_Dict2={}
for len in tmp3:
    my_Dict2.update({len:wtNaive_Dict[len]})

#print(my_Dict)

my_Dict3= {}
for len in tmp:
    my_Dict3.update({len:wtSorted_Dict[len]})

my_Dict4={}
for len in tmp:
    my_Dict4.update({len:wtNaive_Dict[len]})



#dict2csv(my_Dict4,'dict2csv.csv')


###
'''
for i in list(wtTEVsorted):
    if (list(naive).index(i) == -1):
       comp.append(i)
    else:
        comp_R.append(i)
'''
###
#print (tmp2)
#print (len(tmp2))