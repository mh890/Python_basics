'''
students = ["harry" ,"hermione", "ron"]

print(students[1]+ " " + students[0]+ " " + students[2])

#can use a for loop to iterate over strings
for student in students:
    print(student)
'''

'''
Perform following operations on given list
list=[10,20,30,40,50]

Access Elements: Print the third element.
List Length: Print the number of elements in the list
Check if Empty: Write a code to check is list empty.
'''

my_list=[10,20,30,40,50]

print("BASIC LIST OPERATION")
print("Third item in the list: ", my_list[2])
print("Length of the list : ", len(my_list))
if my_list==0:
    print("List is empty")
else:
    print("List is not empty")

'''
Performing list mulitplication
list=[10,20,30,40,50]
Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
'''
print("\n\nList Multiplication")
print("Initial list [10,20,30,40,50]")
my_list.pop(1)
my_list.insert(1, 200)
print("After changing second element", my_list)

my_list.append(600)
print("The list after APPENDING 600: " ,my_list)

my_list.pop(2)
my_list.insert(2, 300)
print("The list after INSERTING 300 at index 2" , my_list)

my_list.remove(600)
print("The list after REMOVING 600: " ,my_list)

my_list.pop(0)
print("The list after REMOVING ELEMENT 0: ", my_list)

'''
Calculate and print the sum and average of all numbers in the list
'''
# built in function alr available
print("\nCalculating the Sum and Average")
list2=[10,20,30,40,50]
tot_sum= sum(list2)
avg= tot_sum/len(list2)

print("Sum is: ", tot_sum)
print("Avg is: ", avg)

'''
Reversing a list
'''
print("\nReversing a List")
list3=[100,200,300,400,500]
list3.reverse()
print(list3)


'''
Turn every element in the list into its square
'''
numbers=[1,2,3,4,5,6,7]

print("\nOutput is the square of each element")
for number in numbers:
    print(pow(number,2), " ", end="")

res=[]
for number in numbers:
    res.append(pow(number,2))
print(res)

'''
finding max and min
'''
#python has built in function for max() and min()
print("\nFinding Maximum and Minimum")
data=[8,2,15,1,9]
print("The largest number: " ,max(data))
print("The smallest number: ", min(data))

'''
Counting number of appearance
i think this can be done using count() function
'''
sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
print("\nCounting number of time 'Football' appears in the list: ", sports.count('Football'))

'''
Sorting --> can be done either by sort() function or sorted() function
'''
numbers = [5, 2, 8, 1, 9]
print("\nSorting a list of numbers")
print("Original list: ", numbers)
print("Sorted list: ", sorted(numbers))

'''
List Manipulation
'''

list4=[1,2,3]
print(list4*2) #output would be 1,2,3,1,2,3

l= "Welcome o Python".split()
print(l) #output --> ["welcome" "o" "python"]


a=[[[1,2],[3,4],5],[6,7]]
print(a[0][1][1])  #output --> 4

a,b=[3,2,1],[5,4,6]
print(a+b) #--> [3,2,1,5,4,6]

my_list2=['p','r','o','b','l','e','m']
print('p' in my_list2) #prints true
print("a" in my_list2) #prints false
print('c' in my_list2) #prints true