#CTI-110
#P2HW2 - List and Sets
#Kyle Blanchard
#06/16/2022
#Display a list that displays lowest numbers to highest numbers in the list and the total of the numbers in the list with the average also showing.

mylist = []

num = float(input("Enter num 1: "))
mylist.append(num)
num = float(input("Enter num 2: "))
mylist.append(num)
num = float(input("Enter num 3: "))
mylist.append(num)
num = float(input("Enter num 4: "))
mylist.append(num)
num = float(input("Enter num 5: "))
mylist.append(num)
num = float(input("Enter num 6: "))
mylist.append(num)
print("Created List")
print(mylist)
smallest = min(mylist)
print("Smallest number in list: ",smallest)

print("Smallest number in list: ",min(mylist))

print("Sum of the numbers in List: ", sum(mylist))

print("Average of numbers in List:", sum(mylist)/len(mylist))

print("Created set")
print(set(mylist))
