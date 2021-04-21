n=int(input("輸入整數n："))
for i in range(n):
    i=i+1
    k=int(input("點與家的距離："))
    if (k%9)==0 or (k%11)==0:
       print("第"+str(i)+"個點："+str(k))