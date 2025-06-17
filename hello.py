#asking user for their name
name = input("whats your name? ")
'''
by default, python ends each statement with newline \n escap cahr but
it can be customnized using end parameter. this allows you to specify
a different string to be printed at the end.

print("Hello")
print("World")

print("Hello", end=" ")
print("World")

Output
Hello
World
Hello World



theres another function called the sep parameter (softspace feature). used for
formatting the output strings
#code for disabling the softspace feature
print('G','F','G', sep='')

#for formatting a date
print('09','12','2016', sep='-')

#another example
print('mujdeh','hosein', sep='@')

Output: 
GFG
09-12-2016
mujdeh@hosein


'''
print("hello," , name, end="") #can either use + or , but using , will already provide the whitespaces between arguments
print(name) 

''' output >>>> hello, mollymolly
'''

print("hello" , name, sep='-')

''' output >>> hello-molly
'''

print(f"hello, {name}") #format string, vs code will recognize it. notice the f before the first set of quotes


#if user enters one too many whitespaces, you can remove all leading and trailing
#use .strip() function --> name= name.strip();

#to capitalize a string, can use .capitalize() function
# name= name.capitalize()
# name = name.title() --> this capitalizes the first letter of each word

#can also combine the functions together
# name= name.strip().title()
# name= input("whats your name?").strip().title()

#can create substrings
first, last = name.split(" ") #sequence unpacking
print(f"hello, ", {last})


