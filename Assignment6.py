print("Enter the number")
'''
a=int(input())
if(a>0):
    print("The %d is positive"%a)
else:
    print("The %d is non positive"%a)

#2nd Question
if(a%5==0):
    print("The number is divisible by 5")
#3
if(a%2==0):
    print("The Number is even")

#4
print("enter second number\n")
b=int(input())
if(a>b):
    print("the greater number between two is %d"%a)
elif(a==b):
    print("Both number %d and %d are same"%(a,b))
else:
    print("the greater number is %d"%b)

#6
print("Enter the number")
n = input()
if(len(n)==3):
    print("Enter number is 3 digit number")
else:
    print("Number is not 3 digit number")'''
#8
print("Enter the values of a,b,c for quardic equation aX^2 + bx + c")
a =int(input())
b =int(input())
c =int(input())
d= b**2 - 4*a*c
if(d>0):
    print("Quardic equation has two real and distinct roots")
elif(d==0):
    print("Quadic has equal roots")
else:
    print("Quardic Equation has imaginary roots")