import math
sumOfList = 0
newNumber = 0

Numbers = [60,61,65,63,98,99,90,95,91,96]

Mean = 0

for x in Numbers:
    Mean = Mean + x
#Adds every number in the list

Mean = Mean/(len(Numbers))
#Gets the mean by dividing the sum of the list

for x in Numbers:
    newNumber= x-Mean
    newNumber = newNumber * newNumber
    sumOfList = sumOfList + newNumber
#Subtracts the mean from every number then squares it and adds the value to a variable

sumOfList = sumOfList/(len(Numbers))
#The variable is devided by the lenght of the list


sumOfList = math.sqrt(sumOfList)
#The variable gets square rooted

print(sumOfList)

