##############################################################################
# 
#       Program Name: madLib.py
#
#       Description: Prompts for user input to complete Mad Lib story
#
#       Language: Python
#
#       Date: 10/14/2022
# 
#       Author: Joshua Farias
#
##############################################################################

def myFallMadLib():
  
  #creates dictionary for words entered by user
  dictionary = [{noun1}, {color1}, {color2}, {adverb1}, {noun2}, {adj1}, {noun3}, {noun4}, {verb1}, {adj2}, {noun5}, {adj3}, {noun6}]
  
#user instructions
print("Enter words to complete the Mad Lib Story!\n")

#assigns user input to variables contained in dictionary defining them
noun1 = str(input("Enter a noun: "))
color1 = str(input("Enter a color: "))
color2 = str(input("Enter a color: "))
adverb1 = str(input("Enter an adverb: "))
noun2 = str(input("Enter a noun: "))
adj1 = str(input("Enter an adjective: "))
noun3 = str(input("Enter a noun: "))
noun4 = str(input("Enter a noun: "))
verb1 = str(input("Enter a verb: "))
adj2 = str(input("Enter an adjective: "))
noun5 = str(input("Enter a noun: "))
adj3 = str(input("Enter an adjective: "))
noun6 = str(input("Enter a noun: "))

#Title
print("\nFall Mad Lib:\n")

#prints out the madlib using f-string interpolation to incorporate dictionary variables
print(f"Fall has arrived with a chill in the {noun1}.")
print(f"The leaves are turning {color1} and {color2}.")
print(f"Night time comes quicker, which usually means {adverb1} {noun2}!")
print(f"But today was a {adj1} day. ")
print(f"My {noun3} went to the nearby {noun4}, where we went on a hay {verb1} to a big {adj2} field, and I even got to pick my own {noun5}!")
print(f"When we get home we'll bake a(n) {adj3} pie and have some {noun6} by the fire. ")
