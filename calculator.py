#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# calculator


def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "*":
        return a * b

    elif operator == "-":
        return a - b

    elif operator == "/":
        return a / b

    elif operator == "**":
        return a**b
    
    else:
        print("Invalid input! Please enter valid integers.")
        return 0


print(
    """MENU
This is an arthematic calculator for solving mathematical calculations
        1. To add two numbers => '+'
        2. To subtract two numbers => '-'
        3. To multiply two numbers => '*'
        4. To divide two numbers => '/'    
"""
)


while True:
    try:
        a = int(input("Enter 1st Number:- "))
        b = int(input("Enter 2nd Number:- "))
        operator = input("Enter The Operator for calculation:- ")
    except Exception as e:
        print(e)
        continue

    output = calculator(a, b, operator)
    while output == 0:
        output = calculator(a, b, operator)
    if output == 1:
        break
    else:
        print(f"The Result is {output}")


# In[ ]:





# In[ ]:




