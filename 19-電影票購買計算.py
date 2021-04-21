p=int(input("請輸入組別數量："))
for i in range(p):
    i=i+1
    a,b=input("第"+str(i)+"組：").split(" ")
    a=int(a)
    b=int(b)
    m=a*250+b*175
    print("第"+str(i)+"組應收費用："+str(m))