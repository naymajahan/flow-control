## Infinite Loop
# Never Ending Loop
#### loop breaking


while True :
    print("Please Enter Your Name:")
    name = input()
    if name == 'Nayma Jahan':
        print("Welcome Nayma Jahan")
        break
print('I am All Yours')


# Continue statement ## CONTINUE STATEMENT

while True :
    print("What is Your Name")
    name = input()
    if name != 'shoshe':
        continue
    print("Hello There," +name+ "-Enter Your Passcode")
    password = input()
    if password == 'astronomy':
        break
print("This is your PC-NAYMA")


## seris ### SERIS ### seris

sum = 0
for i in range(1,5):
    sum = sum+i
print(sum)

# seris 1^1+2^2+3^3+4^4

sum = 0
for i in range(1,5):
    sum = sum+i*i
print(sum)

##### ODD SUM ### ODD SUM
### seris = 1+3+5+7+9

odd_sum = 0
for i in range(1,10,2):
    odd_sum = odd_sum+i
print(odd_sum)


### even seris
### seris= 2+4+6+8

even_sum = 0
for i in range(2,10,2):
    even_sum = even_sum+i
print(even_sum)


### COMPLEX SERIES ////NESTED FOR LOOP/// LOOP UNDER LOOP
#####   complex series = 1+(1+2)+(1+2+3)+(1+2+3+4)


sum = 0
for i in range(1,5):
    for j in range(1,i+1):
        sum = sum+j
print(sum)


