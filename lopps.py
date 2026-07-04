#Countdown Timer
for i in range(10,0,-1):
    print(i)
print("Boom!")    

#Find lucky number  that is divisible by 7
for i in range(1,51):
    if i%7==0:
        print(i)

#Game Score Total
scores=[50,65,70]
total=0
for i in scores:
    total=total+i
print("Total:",total)  

#Multiplication Table
n=5
for i in range(1,11):
    print(n*i)

 #count vowels
word="sivani"
count=0
for ch in word:
    if ch in "aeiouAEIOU":
        count=count+1
print("vowels:",count)  

#Swap numbers
a=10
b=20
print("Before swapping:")
print("a=",a)
print("b=",b)
temp=a
a=b
b=temp
print("After swapping:")
print("a=",a)
print("b=",b)


#ATM
balance=2000
withdrawl_amount=[100,200,150]
for i in withdrawl_amount:
    balance = balance - i
    print("withdrawn:", i)
print("Remaining balance:", balance)


#Finding Highest Marks
marks=[45,78,89,66]
highest=marks[0]
for i in marks:
    if i>highest:
        highest=i
print("Highest Marks:",highest)    

#Number Guess Check
num=25
for i in range(1,51):
    if i==num:
        print("Num found:",i)
        break

#Even number count
count=0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
print("Even numbers:", count)


#Reverse a String
text="sivani"
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Reversed String:", reverse)

    
