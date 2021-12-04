#!/usr/bin/env python
# coding: utf-8

# # que 1 ..simple calculator

# In[4]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x,y):
    return x**y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.power")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# # que 2.. any numeric value in list

# In[44]:


a = [1,'cow',3,'apple']
for i in a:
    if(a[i].isnumeric()==True)
        print("true")


# # que 3.. add a key to dictionary

# In[16]:


a = {1:'a',2:'b', 3:'c'}
key = int(input('enter key : '))
value = input('enter value : ')
a[key] = value
a


# # que 4.. sum all the numeric items

# In[41]:


d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))


# # que 5 .. duplicate values from list

# In[30]:


def checkIfDuplicates(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
result = checkIfDuplicates(listOfElems)
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')  


# # que 6.. if a given key already exist in a dictionary

# In[40]:


a = {1:'a',2:'b', 3:'c',4:'d',5:'e'}
key = int(input('enter key : '))
print(a.get(key,"key not found"))


# In[ ]:




