'''
 It is not necessary to create a CSV file. However, by importing xlrd and csv packages, we can easily convert xlsx to csv.
 Code will be like this:
 workbook = xlrd.open_workbook('1.xlsx')
 table = workbook.sheet_by_index(0) # The int is decided by which table you would like to convert.
 with codecs.open('1.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f)
    for row_num in range(table.nrows):
        row_value = table.row_values(row_num)
        write.writerow(row_value)
'''
import xlrd
import argparse

parser = argparse.ArgumentParser(description = 'There are two arguments required to run this program, which include -gem and -diag. -gem is the path of I10gem, -diag is the path of ICD9 diagnosis file.\n\rYou can run this file with command like this in your command line:\n\rpython Resolving.py -gem ./2018_I10gem.txt -diag ./2015-pdd-diagnosis-code-frequencies20160715.xlsx ')
parser.add_argument('-gem', required = True, type = str,help='Path to the I10gem file')
parser.add_argument('-diag', required = True, type = str,help='Path to the diagnosis file')
args = parser.parse_args()

def get_data(Gemfile,Diagpath):
    pre = {}
    with open(Gemfile, 'r') as f:
        line = f.readline()
        while line:
            line = line.split(' ')
            if len(line) != 3:
                while '' in line:
                    line.remove('')
            if line == []:
                line = f.readline()
                continue
            if line[2][1] == '1':
                line = f.readline()
                continue
            pre[line[0]] = pre.get(line[0], [])
            pre[line[0]].append(line[1])
            line = f.readline()
    workbook = xlrd.open_workbook(Diagpath)
    table = workbook.sheet_by_index(0)
    diag={}
    for row_num in range(1,table.nrows):
        pro=[]
        temp=(table.row_values(row_num)[0].replace('.',''))
        pro=table.row_values(row_num)[1:]
        if pro[1]=='':
            diag[temp] = int(0)
        else:
            diag[temp] = int(pro[1])
    return pre,diag
def map_reduce(Gem,Diag):
    convert=[]
    one=[]
    count=0
    countbase=0
    for each in Gem:
        if len(Gem[each])==1:
            one.append(each)
    for each in one:
        Gem.pop(each)
    for each in Gem:
        print('Converting I10 code: ',each)
        walk=Gem[each]
        base=0
        walks=[]
        flag=0
        for _ in walk:
            if _ in Diag:
                temp=Diag[_]
            else:
                continue
            walks.append((_,temp))
            base+=temp
        if base == 0:
            countbase+=1
            print('No Principal Diagnosis')
            continue
        for i in walks:
            if i[1]/base>0.5:
                convert.append((each,i[0]))
                flag=1
                print('Can be converted to : ',i[0])
        if flag==0:
            count+=1
            print('Can not convert.')
    print()
    print('-------------------------------------Conclusion----------------------------------------')
    print()
    print('Number of I10 code that mapped to many codes of I9: ',len(Gem))
    print('Number of 1:many I10 code that converted to 1:1 code: ',len(convert))
Gem,Diag=get_data(args.gem,args.diag)
map_reduce(Gem,Diag)
