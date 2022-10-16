ages = [10, 20, 30, 40]

def calculateAverage(list):
    sum = 0;
    for i in list:
        sum = sum + i;
    
    return sum/len(list)

print(calculateAverage(ages))
