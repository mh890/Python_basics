x=input("Whats x: ")
y=input("Whats y: ")

#every user input gets registered as a string
h= x+y #this concatenates as a string instead of int

z= int(x) + int(y)

print(h)
print(z)

#Can also do this, this method automatically converts the input into int
m= int(input("WHATS X: "))
n= int(input("WHATS Y: "))
print(m+n)

#floating point value --> number w decimal point
a= float(input("WHATS X: "))
b= float(input("WHATS Y: "))
print(a+b)

#to round the float to the closest int
#use round()

#can create functions to calculate exponents
def main():
    x=int(input("whats x? "))
    print("x squared is", pow(x,2))

main()