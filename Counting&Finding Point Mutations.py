ip1 = input("First sequence:")
ip2 = input("Second sequence:")
ref = ['A', 'G', 'C', 'T', ' ']

list1 = list(ip1)
list2 = list(ip2)

for i in list1:
    ii = i.upper()
    if ii not in ref:
        print("error")  #检查序列1是否合法
        break
for j in list2:
    jj = j.upper()
    if jj not in ref:
        print("error")  #检查序列2是否合法
        break
leng = min(len(list1), len(list2))
n = 0
mut = 0
while n < leng:
    if list1[n] == list2[n]:
        n = n+1
        continue
    else:
        list1[n] = '\033[1;32;40m%s\033[0m' % list1[n]  #   mutation上色标记
        list2[n] = '\033[1;32;40m%s\033[0m' % list2[n]
        n = n+1
        mut = mut+1
re1 = ''.join(list1)
re2 = ''.join(list2)
print(re1+'\n'+re2+'\n'+'total mutations are:'+str(mut))