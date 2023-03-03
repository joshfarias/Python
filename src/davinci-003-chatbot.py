##############################################################################
# 
#       Program Name: davinci-003-chatbot.py
#
#       Description: Simple chatbot using OpenAI's text-davinci-003 model
#
#       Language: Python
#
#       Date: 3/1/2023
# 
#       Author: Joshua Farias
#
##############################################################################

import os
import openai

#read the api key from preset environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

#check if the api key is valid, if not throw error
if not openai.api_key:
    raise ValueError("No OpenAI API key provided. Please set the OPENAI_API_KEY environment variable.")

#welcome message
print("Welcome!\nEnter any prompt or question...")

#init restart_sequence and prompt_text variables
restart_sequence = "\nHuman: "
prompt_text = ""

#starts while loop until the user enters end into prompt
while True:
    user_input = input("You: ")
    if user_input.lower() == "end": #terminates program
        break

    #add user input to prompt text var
    prompt_text += restart_sequence + user_input
    
    #call openai api (text-davinci-003) for interactive chatbot
    response = openai.Completion.create(
        engine="text-davinci-003", #use text-davinci-003 model
        prompt=prompt_text, #set prompt to user input
        temperature=0.9, #controls for randomness and creativity when generating response to user prompt 
        max_tokens=1024, #max number of characters per response (1 ≈ 4 English characters for the text-davinci-003 model)
        top_p=1, #controls for confidence of token generation
        frequency_penalty=0, #discourages model from repeating tokens in response
        presence_penalty=0, #discourages model from generating tokens that aren't in the prompt
        stop=["\nHuman:", "\nAI:"] #signal end of response
    )
    
    message = response.choices[0].text #extract AI response
    prompt_text += message[len(user_input):] #update with each new user prompt
    print("AI:", message.strip()) #print AI's response to console
