a=input("輸入一組四位數字：")
b=list(a)
c=(int(b[0])+7)%10
d=(int(b[1])+7)%10
e=(int(b[2])+7)%10
f=(int(b[3])+7)%10
print("加密後的數字為：",str(e)+str(f)+str(c)+str(d))