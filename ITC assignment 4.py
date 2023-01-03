#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("enter your marks:"))
if 25>=a>=0:
    print("F")
elif 25<=a<45:
    print("E")
elif 45<=a<50:
    print("D")
elif 50<=a<60:
    print("C")
elif 60<=a<80:
    print("B")
else :
    print("A")


# In[2]:


x=int(input("enter an year:"))
if x%4==0:
    print("a leap year")
elif x%100==0 and x%400==0:
    print("a leap year")
else:
    print("non leap year")


# In[ ]:


import random
n=1
while n<11:

    x=(random.randint(0,9))
    print(x)
    y=(random.randint(0,9))
    print(y)
    z=int(input("answer by multiplication:"))
    if z==int(x)*int(y):
        print("good,right answer")
    else:
        print("oops,try again baby ,","right answer is:",x*y)
         
n=n+1


# In[ ]:


x=int(input("guess number of candies:"))
if x%5==2 and x%6==3 and x%7==2:
    print("you guessed the right candies")
else:
    print("you guessed wrong")


# In[ ]:




