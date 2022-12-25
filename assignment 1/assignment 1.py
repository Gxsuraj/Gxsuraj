#Assignment 1

#Soln 1
#Calculating average of three numbers
print("Question 1")
a=int(input("Enter first number-"))
b=int(input("Enter second number-"))
c=int(input("Enter third number-"))
d=(a+b+c)/3
print("The average of the entered numbers is-",d)

#Soln 2
#Finding a person's income tax
print("Question 2")
x=int(input("Enter your Gross Income (in nearest penny)- $ "))  #input of gross income by user
y=int(input("Enter the number of Dependents- "))  #number of dependents
z=x-10000-(y*3000)  #calculating tax income
t=z*0.2  #Total tax
print("Your tax is $ ",t)

#Soln 3
#Number of seconds
seconds=int(input("seconds"))
print(seconds,"s=",seconds//60,"m & ",seconds%60,"s")

#Soln 4
#add three numbers
a=25
b='25'
c=25.0

sum=str(a+ int(b)+ int(c))
print(sum)

#Soln 5
import math 
while(d<=345):
    r=math.radians(d)
    sine=round(math.sin(r),4)
    cosine=round(math.cos(r),4)
    print(d , sine , cosine)
d=d+15  