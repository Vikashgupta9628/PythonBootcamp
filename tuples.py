##Tuples can store the multiple data and data can't be changed
# myTuple= ("Ivan", "Anshu","Mani","Anjali","Mani")
# print(myTuple)
# print(type(myTuple))

# print(myTuple[1])

# # myTuple[1]="Vikash"
# # print(myTuple)

# #It shows error
# #Print values inside TUPLE

# for item in myTuple:
#  print(item)

#Dictionary can store multiple data in key value pair
# myDict ={
#     "keys":"values",
#     "name":"vikash kumar",
#     "email":"brandguptaa8969@gmail.com",
#      "mob":"8969726028"
# }

# print(type(myDict))
# print(myDict)

# for keys in myDict:
#     print(myDict[item])
# print(myDict.get("email"))

# myDict["name"] = "adarsh"
# print(myDict)

#OOPS
#class and object

class Sumeet: 
    age=21
    print("i'm now in Delhi")
    
#Create object and pass class properties
sumeet=Sumeet()
print(sumeet.age)

bornYear = int(input("Enter your born year"))
currentYear =int(input("Enter your current year"))
class AgeCalculator:
    ageInYear= currentYear - bornYear
    dob="8 Oct 2002"
age=AgeCalculator()
print(age.ageInYear,age.dob)
 
#Polymorphism method overloading
def age(dob1):
    print(dob1)
    
def age(dob,name):
    print(dob,name)
    
#x = age("5 Oct 2001")
y = age("29 Feb 2024","Mani Kumar")