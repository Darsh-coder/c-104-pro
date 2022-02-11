import csv

with open("ab.csv",newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newdata = []
for i in range (len(file_data)):
    n_num= file_data[i][1]
    newdata.append(float(n_num))

n = len(newdata)
total = 0
for x in newdata :
    total = total+x

mean = total/n

print("mean or avrage is ",mean)
 






































