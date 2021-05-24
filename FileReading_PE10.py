import FileReading
import pandas as pd 

PE10_Naive = 'TEV-PE10-naive_full.txt'
PE10_Sorted = 'TEV-PE10-sorted_full.txt'

PE10Naive=[]
PE10Sorted=[]
FileReading.txttoList(PE10_Naive,PE10Naive)
FileReading.txttoList(PE10_Sorted,PE10Sorted)

PE10Sorted =[]        
try:
    file=open(PE10_Sorted,"r")     #以读模式打开文件
except FileNotFoundError:          #如果文件不存在，给提示
    print("file is not found")
else:
    contents=file.readlines()       #读取全部行
    for content in contents:       #显示一行
       PE10Sorted.append(content.split('\t')[0])
       # print(content.split('\t')[0])   #每行用逗号(这里是用Tab做分割）分隔后，取第一个元素

PE10Naive =[]        
try:
    file=open(PE10_Naive,"r")     #以读模式打开文件
except FileNotFoundError:          #如果文件不存在，给提示
    print("file is not found")
else:
    contents=file.readlines()       #读取全部行
    for content in contents:       #显示一行
       PE10Naive.append(content.split('\t')[0])
       # print(content.split('\t')[0])   #每行用逗号(这里是用Tab做分割）分隔后，取第一个元素





sorted = set(PE10Sorted)
naive = set(PE10Naive)
NandS = sorted & naive
SminusNandS = sorted - NandS
NminusNandS = naive - NandS



PE10Sorted_Dict = FileReading.csv_to_dict('TEV-PE10-sorted_full.csv')
PE10Naive_Dict = FileReading.csv_to_dict('TEV-PE10-naive_full.csv')
#PESorted = pd.read_csv('TEV-PE10-sorted_full.csv',delimiter='\t') #把csv转换成dataframe的方法

PE10Sorted_List=[]
PE10Naive_List=[]

def forming_df_tmp(dict_name,tmp_name):
    list1=[]
    list2=[]
    for len in tmp_name:
        list1.append(len)
        list2.append(dict_name[len])

    data = {'Sequence':list1,'countings':list2}
    df= pd.DataFrame(data)
    return df


list3=[]
list4=[]
list5=[]
for len in NandS:
    list3.append(len)
    list4.append(PE10Sorted_Dict[len])
    list5.append(PE10Naive_Dict[len])


data = {'sequence':list3,'Sorted_countings':list4,'Naive_countings':list5}


overlapTotal=pd.DataFrame(data)


NonOverlap_Sorted =forming_df_tmp(PE10Sorted_Dict,SminusNandS)
NonOverlap_Naive= forming_df_tmp(PE10Naive_Dict,NminusNandS)
Overlap_Sorted= forming_df_tmp(PE10Sorted_Dict,NandS)
Overlap_Naive= forming_df_tmp(PE10Naive_Dict,NandS)

writer = pd.ExcelWriter('PE10ScatterData.xlsx', engine='xlsxwriter')

overlapTotal.to_excel(writer,sheet_name='Overlap')
NonOverlap_Naive.to_excel(writer,sheet_name='NonOverlap_Naive')
NonOverlap_Sorted.to_excel(writer,sheet_name='NonOverlap_Sorted')

writer.save()

#overlapTotal.to_excel(r'C:\Users\zyzhu\Documents\Rutgers\Spring 2021\昌朋Research\昌朋Research\JOey File\Python\DFtoCSV.xlsx',sheet_name='overlapData')




