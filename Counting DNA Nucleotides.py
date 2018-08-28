inp = str(input("Enter your sequence:"))
l = list(inp)
nl = []
ref = ['A', 'G', 'C', 'T', ' ']
for j in l:
    nj = j.upper()
    nl.append(nj)
for i in nl:
    if i not in ref:
        print("error")  #检查序列是否合法
        break
if i in ref:
    set1 = set(nl)
    dict1 = {}
    for i in set1:
        dict1.update({i:nl.count(i)})    #统计AGCT个数
    print(dict1.get('A'), dict1.get('C') , dict1.get('G'), dict1.get('T'))