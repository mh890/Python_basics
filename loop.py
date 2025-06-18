'''
notes about LOOPS
'''

#WHILE LOOPS
#doesn not require any delimiters, contents are INDENTED and end when indentation ends
i=3
while i!=0:
    print("meow")
    i=i-1 #this updates the value

while i<=3:
    print("meow")
    i+=1

#direct incremment ++ or decrem -- operators DO NOT exist in python
#usually operators like += are used

#FOR LOOP --> python has its own form --> use sqaured brackets
#it ressembles the FOR-EACH loop in java
for _ in range(2): # can use a function in the for loop to make code easier
    print("meow") #underscore is just a convention in python that is used when you dont care about the loop variable

print("meow\n" *3, end="") #string concatenation and formatting



'''
in python, when u want user input that matches a certain expectation you have, use while true
'''

while True:
    n= int(input("Whats n: "))
    if n>0:
        break

for _ in range(n):
    print("meow")

