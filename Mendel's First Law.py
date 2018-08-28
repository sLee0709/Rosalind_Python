def mendel(k,m,n):
    total1 = (((k+m)*(k+m-1))/2)*4  # XX和Xx组合（k组和m组）可形成的无重复组合数
    total2 = (((k+n)*(k+n-1))/2)*4 - (k*(k-1)/2)*4  # XX和xx组合（k组和n组）可形成的无重复组合数
    total3 = (((n+m)*(n+m-1))/2)*4 - ((k*(k-1)+m*(m-1))/2)*4    # Xx和xx组合（m组和n组）可形成的无重复组合数
    total = total1+total2+total3
    yx1 = (m*(m-1))/2*1 # k组和m组中隐性性状数量
    yx2 = (n*(n-1))/2*4 # k组和n组中隐性性状数量
    yx3 = m*n*2 # m组和n组中隐性性状数量
    yx = yx1+yx2+yx3
    return 1 - yx/total

a = int(input("k:"))
b = int(input("m:"))
c = int(input("n:"))
print(mendel(a,b,c))