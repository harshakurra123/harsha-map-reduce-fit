import sys
print(sys.stdin)


for line in sys.stdin:

    datalist = line.strip().split("\t")
    if (len(datalist) == 7) : 
        date, steps, mood, calories, sleep_hours, active, weight = datalist
        weight = datalist[6]
        calories = datalist[3]
        print(weight, "\t", calories)
    