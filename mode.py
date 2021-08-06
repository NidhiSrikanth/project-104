from collections import Counter
import csv
file= open("data.csv",newline="")
reader= csv.reader(file)
filedata= list(reader)

filedata.pop(0)

newdata=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    newdata.append(float(num))

data= Counter(newdata)
modedataforrange= {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0
}

for height, occurance in data.items():
    if 75< float(height) <85:
        modedataforrange["75-85"]+= occurance
    elif 85< float(height) <95:
        modedataforrange["85-95"]+= occurance
    elif 95< float(height) <105:
        modedataforrange["95-105"]+= occurance
    elif 105< float(height) <115:
        modedataforrange["105-115"]+= occurance
    elif 115< float(height) <125:
        modedataforrange["115-125"]+= occurance
    elif 125< float(height) <135:
        modedataforrange["125-135"]+= occurance
    elif 135< float(height) <145:
        modedataforrange["135-145"]+= occurance
    elif 145< float(height) <155:
        modedataforrange["145-155"]+= occurance
    elif 155< float(height) <165:
        modedataforrange["155-165"]+= occurance
    elif 165< float(height) <175:
        modedataforrange["165-175"]+= occurance

moderange, modeoccurance= 0,0
for range,occurance in modedataforrange.items():
    if occurance> modeoccurance:
        moderange, modeoccurance= [int(range.split("-")[0]), int(range.split("-")[1])], occurance
    
mode= float((moderange[0]+ moderange[1])/2)
print(mode)

