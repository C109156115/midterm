m=int(input("請輸入階層值M："))
tt=1
n=1
while tt<m:
    tt=tt*n
    if tt>m:
        break
    n=n+1
print("超過M值為"+str(m)+"的最小階層n值為："+str(n))