# EX1
minNumber = int(input())
maxNumber = int(input())
if maxNumber > minNumber:
    for n in range(minNumber,maxNumber,2):
        print(n)
else:
    print("nothing")


# EX2
text = input()
number = ""
sumNumber = 0
for n in range(len(text)):
    if text[n].isnumeric():
        number += text[n]
    elif len(number) > 0:
        sumNumber += int(number) 
        number = ""
if len(number) > 0 :
    sumNumber += int(number)
print(sumNumber)  


# EX3
text = input()
newArray = []
result = ""
for i in range(len(text)):
    if text[i] == " ":
        newArray.append(result)
        result =""
    else:
        result += text[i]
if len(result) !=0 :
    newArray.append(result)
print(newArray)  


# EX4
array = eval(input())
result = 0
for dic in array:
    result += dic['price']* dic['quantity']
print(result) 


# EX5
array1 = eval(input())
array2 = eval(input())
sum1 = 0
sum2 = 0
result = 0
for i in range(len(array1)):
    sum1 += array1[i]
for n in range(len(array2)):
    sum2 += array2[n]
if sum1 > sum2:      
    result = array1
elif sum2 > sum1:
    result = array2
else:
    result = "equal"
print(result)  


# EX6
array = eval(input())
sumOfNumber = 0
for index in array:
    if index <= 10:
        sumOfNumber += index
print(sumOfNumber)


# EX7
dic = {}
result = True
while result:
    name = input() 
    if name != "end":
        number = int(input())
        dic[name] = number
    else:
        result = False
print(dic)


#EX8
def getHospitalForNewPatient(maxBedsPerHospital, personnsPerHospital):
    for key in maxBedsPerHospital:
        if (maxBedsPerHospital[key]) != len(personnsPerHospital[key]):
            return key
    return None
persons = eval(input())
maxBedsPerHospital = eval(input())
personnsPerHospital = {}
for name in maxBedsPerHospital:
    personnsPerHospital[name] = []
for key in persons:
    personnsPerHospital[getHospitalForNewPatient(maxBedsPerHospital,personnsPerHospital)].append(key)
print(personnsPerHospital)


#EX9
personsInRoom = eval(input())      # it's an array 2D !
newPersonRow = int(input())        # row of the new person to add
newPersonColumn = int(input())     # column of the new person to add
count = 0
result = ""
for row in personsInRoom:
    for column in row:
       if column == 1:
            count += 1         
if personsInRoom[newPersonRow][newPersonColumn] == 1 or count == 3:
    result = "CANNOT ADD"
else:
    result = "CAN ADD"
print(result)


#EX10
def isEqual(array1, array2):
    #write your code here
    if len(array1) == len(array2):
        for index in range(len(array1)):
            if array1[index] != array2[index]:
                return False
    else:
          return False      
    return  True
array1 = eval(input())
array2 = eval(input())
#call your function here
if isEqual(array1,array2):
    print("EQUAL")
else:
    print("NOT EQUAL")

    
#EX11
# MAIN CODE 
array = eval(input())
newArray = []
# Write your code here !
for column in range(len(array[0])):
    sumOfNumber = 0
    for row in range(len(array)):
        sumOfNumber += array[row][column]
    newArray.append(sumOfNumber)
print(newArray)