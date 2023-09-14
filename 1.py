import csv
f=open("sns_use.csv","r",encoding="euc-kr")
data=csv.reader(f)
next(f)
facebook=[]
for row in data:
    facebook.append(float(row[2]))
print(facebook)
f.close()




