'''
Joshua Farias
COMSC230
Professor Morales
Midterm #1
ATMJF.py
Description: 
Simulate an ATM.
- Each user has checking/savings accounts
- password
- 5 option menu:
deposit, withdraw, transfer, check balance, exit
- display transaction ledger at end of program
'''
#imported system class to call sys.exit() to terminate program 
#once login attempt limit is reached or to handle errors
import sys

#imports bankUserJF class that defines objects in relation to:
#account numbers, passwords, names and bank balances
from bankUserJF import bankUserJF

#defines print menu argument which displays user options
def print_menu():    
    print("\nGold Credit ATM Menu:\n")
    print("1. Make deposits")
    print("2. Make withdrawals")
    print("3. Make transfers")
    print("4. See balance")
    print("5. Exit")
    
#defines deposit function    
def deposit(bankUserJF):
    try:
        #displays the deposit menu
        print("\nDeposit Menu: \n")
        #prompts user for account type
        accType = str(input("Which account type? (Enter 'checking' or 'savings'): "))
        #makes user input case insensitive
        if(accType.casefold() == "savings"):
            #creates deposit variable as user input which is stored as float (for decimal values)
            deposit = float(input("How much would you like to deposit?: $"))
            #updates the savings account with what the user deposited
            if(deposit < 0):
                print("Can not deposit negative value. Please try again.\n")
            else:
                bankUserJF.set_savings(bankUserJF.get_savings() + deposit)
                deposit.count()
                #displays updated balance to the user
                print("Your new balance is: $", str(bankUserJF.get_savings()))
                print("Thank you for doing business with Gold Credit!")
        #makes user input case insensitive
        if(accType.casefold() == "checking"):
            #creates deposit variable as user input which is stored as float (for decimal values)
            deposit = float(input("How much would you like to deposit?: $"))
            #updates the checking account with what the user deposited
            if(deposit < 0):
                print("Invalid entry. Please try again.\n")
            else:
                bankUserJF.set_checking(bankUserJF.get_checking() + deposit)
                print("Your new balance is: $", str(bankUserJF.get_checking()))
                print("Thank you for doing business with Gold Credit!")
    except:
        #if input is not float program displays error message below, resets then displays main menu
        print("Invalid entry. Please try again.\n") 

#defines withdrawal function
def withdraw(bankUserJF):
    try:
        #displays withdrawal menu
        print("\nWithdrawal Menu: \n")
        #prompts user for account type
        accType = str(input("Which account type would you like to withdraw from? (Enter 'checking' or 'savings'): "))
        #makes savings case insensitive
        if(accType.casefold() == "savings"):
            #prompts user for the amount they would like to withdraw from savings
            withdraw = float(input("How much would you like to withdraw?: $"))
            if(withdraw < 0):
                print("Can not withdraw negative value. Please try again.")
            #if withdrawal request is greater than $400 program resets
            elif(withdraw > 400):
                print("Sorry, you can only withdraw up to $400 at a time.\nPlease try again.")
            #if withdrawal request is more than what is in savings account program resets
            elif(bankUserJF.get_savings() < withdraw):
                print("You have insufficient funds. Please try again.")
            #if withdrawal request is less than $400 and is not more than what is in account
            #the request processes successfully and the new balance is displayed to user
            else:
                bankUserJF.set_savings(bankUserJF.get_savings() - withdraw)
                print("You have successfully withdrawn $", str(withdraw))
                print("Your new savings account balance is: $", str(bankUserJF.get_savings()))
        #makes checking case insensitive    
        if(accType.casefold() == "checking"):
            #prompts user for the amount they would like to withdraw from checking
            withdraw = float(input("How much would you like to withdraw?: $"))
            if(withdraw < 0):
                print("Can not withdraw negative value. Please try again.")
            elif(withdraw > 400):
                print("Sorry, you can only withdraw up to $400 at a time.\nPlease try again.")
            elif(bankUserJF.get_checking() < withdraw):
                print("You have insuffient funds. Please try again.")
            else:
                bankUserJF.set_checking(bankUserJF.get_checking() - withdraw)
                print("You have successfully withdrawn $", str(withdraw))
                print("Your new balance is: $", str(bankUserJF.get_checking()))
    except:
        print("Invalid entry. Please try again.")
        
def transfer(bankUserJF):
    try:
        #displays transfer menu
        print("\nTransfer Menu: \n")
        #prompts user for account they would like to transfer from
        accType = str(input("Which account type would you like to transfer from? (Enter 'checking' or 'savings'): "))
        if(accType.casefold() == "savings"):
            #prompts user for amount they would like to transfer
            transfer = float(input("How much would you like to transfer?: $"))
            #if user tries to transfer more than they have program resets
            if(bankUserJF.get_savings() < transfer):
                print("You have insufficient funds. Please try again.")
            else: #transfer gets processed, accounts are updated and displayed to user
                bankUserJF.set_savings(bankUserJF.get_savings() - transfer)
                bankUserJF.set_checking(bankUserJF.get_checking() + transfer)
                print("You have successfully transfered $", str(transfer), "to your checking account.")
                print("Your updated savings balance is: $", str(bankUserJF.get_savings()))
                print("Your updated checking balance is: $", str(bankUserJF.get_checking()))
        #transfer from checking to savings   
        if(accType.casefold() == "checking"):
            transfer = float(input("How much would you like to transfer?: $"))
            if(bankUserJF.get_checking() < transfer):
                print("You have insufficient funds. Please try again.")
            else:
                bankUserJF.set_checking(bankUserJF.get_checking() - transfer)
                bankUserJF.set_savings(bankUserJF.get_savings() + transfer)
                print("You have successfully transfered $", str(transfer), "to your savings account.")
                print("Your updated checking balance is: $", str(bankUserJF.get_checking()))
                print("Your updated savings balance is: $", str(bankUserJF.get_savings()))
    except:
        print("Invalid entry. Please try again.")
        
#displays the users banking balances by getting the updated object values        
def check_balance(bankUserJF):
    print("Savings: $", bankUserJF.get_savings())
    print("Checking: $", bankUserJF.get_checking())
    print("Total: $", bankUserJF.get_savings()+ bankUserJF.get_checking())
    
    
#conditional statement that allows imported code to run    
if __name__ == "__main__":

    #creates a list containing 6 objects as defined in bankUser class
    curent_user = bankUserJF("","","","","","")
    
    #generates list of bank members
    listOfBankMembers = []
    #the list is hardcoded with the users account #, password, name, saving and checking balances (defaulted with $1000 each)
    listOfBankMembers.append(bankUserJF("99999230","0230","Joshua","Farias", 1000.00, 1000.00))
    
    #wrong user input counter
    counter = 0
    
    #creates accNum variable and sets the value to null
    accNum = ""
    while True:
        try:
            accNum = input("Please enter your account number: ")
            #accNumMatch is a variable that represents valid account numbers contained in the list of bank members
            accNumMatch = [member for member in listOfBankMembers if member.accNum == accNum]
            #if user enters an account number that is found within the list of bank members
            #they are permitted to proceed
            if(len(accNumMatch) > 0):
                current_user = accNumMatch[0]
                break
            #if the user password is incorrect
            else:
                #the counter increments by 1
                counter += 1
                #tells the user they have entered the wrong information
                print("Account number was not recognized.")
                print("You have", 3 - counter,"attempts remaining" )
                #once the increment hits 3 the program terminates
                if(counter == 3):
                    print("Attempt limit reached. ATM shutting down...")
                    sys.exit()
        except: #handles errors by terminating program
            sys.exit()
                 
    while True:
        try:
            #prompts user for password
            userPwd = input("Please enter your password: ")
            #if password is valid they are permitted
            if(current_user.get_pwd() == userPwd):
                break
            else: #if password is invalid 
                print("Invalid password.\n")
                counter += 1 #counter increments by 1
                print("Password was not recognized. Please try again.")
                print("You have", 3 - counter,"attempts remaining" )
                if(counter == 3): #program terminates once increment hits 3
                    print("Attempt limit reached. ATM shutting down...")
                    sys.exit()
        except:
            sys.exit()
            
#displays welcome message for user containing the name associated with their account            
print("\nWelcome,", current_user.get_firstname(), current_user.get_lastname())

#creates option variable
option = 0

while(option != 5):
    print_menu()
    try:
        #sets option variable to equal user input
        option = int(input("\nEnter a number to make a selection: "))
    except:
        print("Invalid input. Please try again.")
    #sets user to specific menu in relation to number entered    
    if(option == 1):
        deposit(current_user)
    elif(option == 2):
        withdraw(current_user)
    elif(option == 3):
        transfer(current_user)
    elif(option == 4):
        check_balance(current_user)
    elif(option == 5):
        break
    #if options are not in range of 1-5 bank menu resets
    else:
        print("Invalid entry.")
        option = 0
        
#displays transaction ledger from recent banking session upon program exit
print("Transaction Ledger from recent session:")
print('transactionNumber' + 5*' ' + 'accountType' + 5*' ' + 'transactionAmount') # 5*' ' adds 5 spaces in between each string
print("\nThank you for using Gold Credit!")