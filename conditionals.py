''''
>
>=
<
<=
==
!=
'''

x= int(input("Whats x: "))
y= int(input("Whats y: "))


#IF STATEMENT
if x<y:
    print("x is less than y")
if x>y:
    print("x is greater than y")
else:
    print("they are of same value")

#ELIF STATEMENT
a= int(input("whats a: "))
b= int(input("whats b: "))
if a<b:
    print("a is less than b")
elif a>b:
    print("a is greater than b")
elif x==y:
    print("the same")


'''
python does not have a switch- case statement
either use a dictionary or implement if-else statements
you can also use MATCH STATEMENT, which is in the new Python
'''
#MATCH STATEMENT
name= input("whats your name? ")
match name:
    case "harry" | "another harry name idk": #you can use conditionals in the match
        print("harrys house")
    case "hermione":
        print("herminone house")
    case "ron":
        print("rons house")
    case "draco":
        print("slytherin")
    case _: #this means default case or match with anything else, the underscore is a wildcard --> doesnt care what the value is
        print("who? ")    

