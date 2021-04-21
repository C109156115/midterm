dict1={"金":4,"銀":5, "銅":9, "優":7}
item1=list(dict1.items())
for name,num in item1:
    print("%s牌得到 %d 面" % (name, num))