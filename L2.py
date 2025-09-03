# check a sub string of a another stirng 
txt = "The best thinks in life are free!"
print("free" in txt) #method 1
if "free" in txt: # method 2 if statement se
    print("Yes, 'free' is present.")

print("hello" not in txt) #hello is not present in txt so coming out true

#Slicing string
b= "Hello, world!"
print(b[2:5]) #end index excluding hai and start wala including hai
print(b[:5]) #by default 0->5 where index 5 is excluding
print(b[2:]) #by default 2->end
print(b[-5:-2]) # in -ve index oprate from end 2->5 (end se  OR reverse me)


#Modify Strings
a,b="bibit","SINGH"
print(a.upper())
print(b.lower())
print(a.strip())
print(a.replace('b','B')) #replacing
print(a.split(","))# spliting in word 

# Formate String
age=20
# txt = "my name is bibit , my age is" + age wrong method
txt = f"my name is bibit , my age is {age}" #use f syntex in begin
print(txt)