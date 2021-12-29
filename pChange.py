#!/usr/bin/python
c1 = float(input("Enter the current price: "))
f1 = float(input("Enter the final price: "))
v1 = (f1 - c1) / c1
print("%.0f%%" % (100 * v1))
input('Press Enter to Exit')
