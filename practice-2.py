#1st problem
#A program to check a year is leap year or not ???
## SOLUTION

print('Input a Year:')
year = input()
yEar = float(year)
if yEar % 400 == 0:
    print("This is a Leap Year")
elif yEar % 100 == 0:
    print("This is not a Leap Year")
elif yEar % 4 == 0:
    print("This is a Leap Year")
else:
    print("This is not a Leap Year")


#2nd problem 
## Printing Patterns 
# 1st pattern
#   *
#  ***
# *****
#*******
##### Solution 

print(end="   " +"*\n")
print(end="  " +"***\n")
print(end=" "+ "*****\n")
print("*******")

#2nd Pattern
#   *
#  **
# ***
#****
#### SOLUTION

print(end="   " +"*\n")
print(end="  " +"**\n")
print(end=" " +"***\n")
print("****")

##### 3rd PROBLEM  ####
# Check a number is armstrong or not
### SOLUTION FOR 3 DIGIT NUMBER RANGE


print('enter a number')
number = int(input())
digit = number
sum = 0
while number != 0:
    remainder = number%10
    number = number//10
    sum = sum+remainder**3

if sum == digit:
    print('This is an Armstrong Number')
else:
    print('This is not an Armstrong Number')

    