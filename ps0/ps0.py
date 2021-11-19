"""
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""

import numpy as np
x=int(input("Enter number x:"))
y=int(input("Enter number y:"))
power=x**y
print("x ** y:"+str(power))
log_x=np.log2(x)
print("log(x):"+str(log_x))



