
import sys

thisKey = ""
thisValue = 0.0
count = 0

for line in sys.stdin:
    dataList = line.strip().split('\t')
    if(len(dataList)==2):
        weight, calories = dataList

        if weight != thisKey:
            if thisKey:
               print(thisKey,'\t',thisValue/count if count > 0 else 0)

            thisKey = weight
            thisValue = 0.0
            count = 0

        thisValue += float(calories)
        count+=1

print(thisKey,'\t',thisValue/count if count > 0 else 0)