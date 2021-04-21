m=int(input("小明身上有幾元："))
n=int(input("販賣機有幾種飲料："))
t=0
for i in range(n):
    p=int(input("飲料價格:"))
    if (m/p)>=1:
       t=t+1
print(t)