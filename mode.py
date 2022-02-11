import csv
from collections import Counter
from statistics import mode 
with open("ab.csv",newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newdata = []
for i in range (len(file_data)):
    n_num= file_data[i][1]
    newdata.append(float(n_num))

data = Counter(newdata)
mode_data_for_range = {
"75-85":0,
"85-95":0,
'95-105':0,
'105-115':0,
"115-95":0,
'125-105':0,
'135-115':0,
"145-95":0,
'155-105':0,
'165-115':0,
"165-175":0,

}

for height,occournce in data.items():
    if 75 <float(height)<85 :
        mode_data_for_range["75-85"]+=occournce
    elif 85 <float(height)<95 :
        mode_data_for_range["85-95"]+=occournce
    elif 95 <float(height)<105 :
        mode_data_for_range["95-105"]+=occournce
    elif 105 <float(height)<115 :
        mode_data_for_range["105-115"]+=occournce
    elif 115 <float(height)<125 :
        mode_data_for_range["115-125"]+=occournce
    elif 125 <float(height)<135 :
        mode_data_for_range["125-135"]+=occournce
    elif 135 <float(height)<145 :
        mode_data_for_range["135-145"]+=occournce
    elif 145 <float(height)<155 :
        mode_data_for_range["145-155"]+=occournce
    elif 155 <float(height)<165 :
        mode_data_for_range["155-165"]+=occournce
    elif 165 <float(height)<175 :
        mode_data_for_range["165-175"]+=occournce
    

moderange,modeoccourance = 0,0

for range,occournce in mode_data_for_range.items():
    if occournce > modeoccourance :
        moderange,modeoccourance=[int(range.split("-")[0]),int(range.split("-")[1])],occournce


mode = float((moderange[0]+moderange[1])/2)


print(mode)






