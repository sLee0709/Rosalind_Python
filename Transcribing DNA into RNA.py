a = list(str(input("Enter your sequence:")))
ref = ['A', 'G', 'C', 'T', 'a', 'g', 'c', 't', ' ']
for i in a:
    if i not in ref:
        print("error")  #检查序列是否合法
        break
if i in ref:
    new_l = ['u' if i == 't' else 'U' if i == 'T' else i for i in a]    #T转U
    print(''.join(new_l))