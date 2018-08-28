n = int(input("n:"))
k = int(input("k:"))
alist = [1,1]
i = 2
if i >= n:
    print(1)
while n > i:
    a = alist[i-1] + k*alist[i-2]
    alist.append(a)
    i+=1
    if n == i:
        print(alist[n-1])