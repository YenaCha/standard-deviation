import csv
import math
with open('data.csv') as f:
    csvreader = csv.reader(f)
    filedata = list(csvreader)
data = filedata[0]

sum = 0
for s in data:
    sum = sum+int(s)
mean = sum/len(data)

sum = 0
for s in data:
    a = int(s)-mean
    b = a*a
    sum = sum+b
d = sum/(len(data)-1)
sq = math.sqrt(d)
print(sq)