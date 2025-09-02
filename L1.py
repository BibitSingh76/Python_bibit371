#comments in python using # AND """ """
print("hello ji")
"""print("hef")
hello everyone"""

#variable in python
counter=100
miles=1000.0
name="bibit"
print(counter)

# deleting variable in python
#you can delete multiple variable at a time


# del counter
# del miles,name
# print(counter)
# print(name)

#getting a type of variable in python using built-in function type()


print(type(name))
print(type(miles))
print(type(counter))

#casting in python variable


x=str(10)  #x will be '10'
y=int(10) # y will be 10
z= float(10) #x will be 10.0
print("x =",x)
print("y =",y)
print("z =",z)

#Python variables are case sensitive which means Age and age are different
Age=20
age=30
print(Age,age)

#python allows to initialize more than one variables in a single statement 
#if value is same 
a=b=c=10
#if values are different
a,b,c=10,20,30
print(a,b,c)

#Multi Words variable Names=>these are three types

# Camel Case -> myVariableName="bibit"
# Pascal Case -> MyVariableName="bibit"//-> check (sirf class me hi use hota hai)
# Snake Case -> my_variable_name="Bibit"

#list in python it can be store multiple types of data type
my_list=[] #empty list
numbers = [1,2,3,4,5] # list with numbers
mixed = [10,"hello",2.14,True] # list with mixed data
nested =[[2,3],[2,5]] #nested list
print(mixed[2])
for i in numbers:
    print(i)