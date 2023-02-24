##############################################################################
# 
#       Program Name: DALLEImageGenerator.py
#
#       Description: Generates a 256x256 image based on user input using
#       OpenAI's DALL-E AI image generator. 
#
#       Language: Python
#
#       Date: 2/24/2022
# 
#       Author: Joshua Farias
#
##############################################################################

import os
import openai

#read the api key from preset environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

#check if the api key is valid
if not openai.api_key:
    raise ValueError("No OpenAI API key provided. Please set the OPENAI_API_KEY environment variable.")

#prompt the user for an image prompt
prompt = input("Enter a prompt for DALL-E (Ex: 'a flying whale in outerspace 4k photorealistic'): ")

#handles empty prompt
if not prompt:
    print("Prompt cannot be empty. Please try again.")
    exit()

#call openai api (dall-e) to generate the image
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256"
)

#print the response url for the generated image
print(f"Generated image URL: {response.data[0].url}")
