#!/usr/bin/env python
# coding: utf-8

# # Python BMI Calculator

# Under 18.5--> Underweight 
# 18.5 - 24.9-> Normal Weight/Minimal 
# 25 - 29.9---> Overweight/Increased
# 30 - 34.9---> Obese/High
# 35 - 39.9---> Severely Obese/Very High
# 40 and over-> Morbidly Obese/Extremely High

# In[16]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0:
    if(BMI < 18.5):
        print(name +", you're under weight.")
    elif(BMI <= 24.9):
        print(name + ", you're a normal weight.")
    elif(BMI <= 29.9):
        print(name +", you're Overweight.")
    elif(BMI <= 34.9):
        print(name + ", you're Obese.")
    elif(BMI <= 39.9):
        print(name + ", you're Severely Obese.")
    else:
        print(name + ", you are morbidly Obese.")
else:
        print("Enter valid input")


# In[ ]:





# In[ ]:





# In[ ]:




