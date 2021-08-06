import csv
file= open("data.csv",newline="")
reader= csv.reader(file)
filedata= list(reader)

filedata.pop(0)

newdata=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    newdata.append(float(num))

n= len(newdata)
total=0
for i in newdata:
    total= total+i 

mean= total/n 
print(mean)
