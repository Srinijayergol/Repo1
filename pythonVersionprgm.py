import sys
from datetime import *
import time
from math import pi

print("=================================================")
print("First type of printing python version information")
print("Python Version is : \n"+format(sys.version))
print("Python version info:\n"+format(sys.version_info))
print("==================================================")
print("Second type of printing python version information")
a,b = sys.version,sys.version_info
print("Python version: \n" + a + "\n" + "Python version info:\n" +str(b))
print("==============================")
print("Printing current date and time:")
d= datetime.now()
print (d.strftime("%Y-%m-%d %H:%M:%S"))
print("===============================")
print("Enter the radius value: ")
radius = float(input())
area = pi * radius**2
print("Area of circle with radius "+ str(radius)+ " is : "+str(area))
print("===============================")
values = input("Enter the numbers: \n")
values_input = values.split(",")
list = list(values_input)
print("The list representation of numbers is: "+str(list))
tuple = tuple(list)
print("The tuple representation of numbers is: "+str(tuple))
print("================================")
print("Enter the filename with extensions: ")
input_value = input()
split_value = input_value.split(".")
output_value = split_value[1]
print("File name is with ."+str(output_value)+" extension")
print("================================")
print("Enter the color set: ")
values = input()
list = values.split(",")
print("The first and last color values are: ")
print(list[0], list[-1])
print("===================================")
print("Enter the integer value: ")
n1= int(input())
n2= int("%s%s" %(n1,n1))
n3= int("%s%s%s"%(n1,n1,n1))
expression = n1+n2+n3
print("The value after adding is: "+str(expression))
print("===================================")
