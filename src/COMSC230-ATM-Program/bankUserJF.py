'''
Joshua Farias
COMSC230
Professor Morales
Midterm #1
bankUserJF.py
Description: 
Class that creates objects associated with bank users
'''

#class that initializes accNum, pwd, firstname, lastname, savings, checking objects
class bankUserJF():
    def __init__(self, accNum, pwd, firstname, lastname, savings, checking):
        #values are set to be defined in main program (hardcoded in)
        self.accNum  = accNum
        self.pwd = pwd
        self.firstname = firstname
        self.lastname = lastname
        self.savings = savings
        self.checking = checking
    
    #getter methods for account number, password
    #name, checking and savings balances       
    def get_accNum(self):
        return self.accNum
    def get_pwd(self):
        return self.pwd
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_savings(self):
        return self.savings
    def get_checking(self):
        return self.checking
    
    #setter methods for account number, password
    #name, checking and savings balances  
    def set_accNum(self, newVal):
        self.accNum = newVal
    def set_pwd(self, newVal):
        self.pwd = newVal
    def set_firstname(self, newVal):
        self.firstname = newVal
    def set_lastname(self, newVal):
        self.lastname = newVal
    def set_savings(self, newVal):
        self.savings = newVal
    def set_checking(self, newVal):
        self.checking = newVal