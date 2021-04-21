T=int(input("請輸入班級數量："))
c=[]
for i in range(T):
    n=int(input("請輸入班級人數："))
    c.append(n)
c.sort()
c.reverse()
print(c[0])

    