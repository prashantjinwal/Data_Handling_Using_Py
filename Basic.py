

name = "Tony stac"
age = 45
Quo = "Tony is genius"
print(name, "age is" , age , "and he is a" , Quo)  

naam = input("enter your name")
print("hello my name is " + naam)  


old_age = "55"
new_age = int(old_age) + 2

print(new_age)

num = 30
print(float(num))

num1 = 44
num2 = 43
sum = num1 + num2 
print("The sum is : " + str(sum))

user = "prashant"
print(user.find("h"))
print('r' in user)

print(24 / 5)
print(24 // 5)

print( 23 > 3 or 4 > 5 )
print( 23 > 3 and 4 > 5 )

age = 16 
if age > 5 : 
    print("yoyo") 
    
elif age < 17 : 
    print("fuds")
    
    
i = 1
while i < 15 :
    print(i)
    i = i + 1


for item in range(5) :
    print(item)

# ----list----
marks = [2,53,5,43, "math"]
print(marks)
print(marks[3])
print(marks[-2])
print(marks[-4])


marks = [2,53,5,43,8,87,44,33]
for mark in marks : 
    print(mark + 1)
    
marks.append(53)

for mark in marks : 
    print(mark)
    
print(99 in marks)
print(53 in marks)

print(len(marks))

i = 1
while i < len(marks) :
     print(i)
     i = i + 1
     
print(type(marks))

for mark in marks : 
    if mark == 44 : 
        break
    if mark == 5 : 
        continue
    print(mark)
    

# tuples is similar as list but we dont change tuple items in run and compile time 
numbers = (23,4,33,4,455)
print(numbers.count(4))    
print(numbers.index(4))         #find index of tuple

# ---- list[]   ,  tuple() ,   set{}  ------


# Dictionary

result = {"english" : 55 , "math" : 78 , "chemistry" : 98}

print(result["chemistry"])

result["physics"] = 84
print(result["physics"])


# ------ Function ------
# 1 -> in built function.
# 2 -> user defined function.
def printSum(first , second = 3):
    sum = first + second
    print(sum)

printSum(3)

# 3 -> module function.
# import math
# from math import *
# # print(dir(math))
# print(sqrt(4))

