##############################################################################
# 
#       Program Name: passwordGenerator.py
#
#       Description: Generates a secure 15 character password
#
#       Language: Python
#
#       Date: 11/9/2022
# 
#       Author: Joshua Farias
#
##############################################################################

import random
import string

def generate_password(length=15):
    #define the possible characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #generates password by selecting random characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    password = generate_password()
    print(password)
