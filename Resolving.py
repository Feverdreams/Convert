import xlrd
import csv
'''workbook = xlrd.open_workbook('2015-pdd-diagnosis-code-frequencies20160715.xlsx')
table = workbook.sheet_by_index(0)
with open('diagnosis.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f)
    for row_num in range(table.nrows):
        row_value = table.row_values(row_num)
        write.writerow(row_value)'''
pre=[]
with open('diagnosis.csv', 'r') as f:
     line=f.readline()
     line=f.readline()
     while line:
         if line=='\n':
             line=f.readline()
             continue
         line=line.split(',')
         line[0]=line[0].replace('.','')
         other=line[3:-1]
         sum=0
         for each in other:
             if each!='':
                sum+=float(each)
         if line[2]=='':
             line[2]=0
         res=[]
         res.append(line[0])
         res.append(int(float(line[1])))
         res.append(int(float(line[2])))
         res.append(int(sum))
         pre.append(res)
         line=f.readline()
print(pre[:100])