
import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
    dataList = line.strip().split('\t')
    if(len(dataList)==2):
        weight, calories = dataList

        if weight != thisKey:
            if thisKey:
               print(thisKey,'\t',thisValue)

            thisKey = weight
            thisValue = 0.0

        thisValue += float(calories)

print(thisKey,'\t',thisValue)