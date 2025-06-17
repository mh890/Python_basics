'''
this is to use functions, can make our own too
use def for define and to create functions
if ur using a function, it must alr exist by the time its being called
so therefore, define all the functions you need at the beginning


always call main() at the end of the file
'''

def funct():
    print("hello") #it automatically indents to 4 whitespaces


#can parameterize the function too
def funct(to):
    print("hello," , to)


#can assign a default value too

def funct(to='world'):
    print("hello" , to)

funct()
name = input("Whats your name? ")
funct(name)


'''
in terms of scope, python has three different ones: local, global and nonlocal
a variable scope specifies the region where we can access a variable

LOCAL SCOPE
when a variable is declared inside a function, these variableswil have a local scope
--> they cannot be accessed from outside the function
'''
def greet():
        msg="hello"
        print(msg)
    
greet()

##print(msg) #this will produce an error
#here, msg variable is loval to the function greet() and can only be accessed within the variable
#to fix this issue, you have to make it a global variable

'''
GLOBAL VARIABLE
its a variable devlared outside the function or in the global scope
can be accessed inside or outside of the function
'''

# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

#output >> Local Hello \nGlobal Hello


