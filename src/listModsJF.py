'''
Joshua Farias
COMSC230
Professor Morales
Assignment #3
listModsJF.py
Description: 
Displays and interactive menu that allows
the user to sort, reverese, delete and reduce
the given list.
'''

list = [] #creates empty list

elementPrompt = int(input("Enter total number of elements: ")) #prompts user to input elements into list

#iterates each element being entered into list
for i in range(0, elementPrompt):
    ele = int(input("Enter an element: "))
    list.append(ele)
print("\nYour List: ")
print(list, "\n")

#creates menu
def menu():
    print("1 -  Sort the list")
    print("2 -  Reverse the list")
    print("3 -  Delete/empty the list")
    print("4 -  Reduce the list")    
menu()


#prompts for user menu option
userOption = int(input("Enter your option: "))

while userOption != 0:
    
    #sorts list in ascending order
    if userOption == 1:
        list.sort()
        print("Sorted list: " +str(list))
        
    #reverses list
    elif userOption == 2:
        list.reverse()
        print("Reversed list: " +str(list))
        
    #clears the list
    elif userOption == 3:
        list.clear()
        print("Emptied List: " +str(list))
        
    #reduces the list by adding all of the elements together
    elif userOption == 4:
        reducedList = sum(list) #calculates sum of list
        list.clear() #empties list
        list.append(reducedList) #appends sum to empty list
        print("Reduced list: " +str(list))
    else:
        print("Invalid entry, please try again.")
        
    print()
    (menu)
    
    userOption = int(input("Enter your option: "))