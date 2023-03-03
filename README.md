<h1>
  <img src="https://github.com/joshfarias/Python/raw/main/images/python-logo.png" alt="python logo" height="100">
 </h1>

## Chatbot using text-davinci-003 Model from OpenAI
**[davinci-003-chatbot.py](https://github.com/joshfarias/Python/blob/main/src/davinci-003-chatbot.py)**

This program uses [OpenAI's API](https://openai.com/blog/openai-api) to generate responses to user prompts and questions in an interactive chatbot format. The responses generated are based on OpenAI's text-davinci-003 language model. To end the chat the user can enter the keyword `end`.

Below is an screenshot containing a brief conversation with the chatbot:

<h1>
<img src="https://github.com/joshfarias/Python/blob/main/images/davinci-003-chatbot.png" alt="python logo" height="400">
</h1>

### Notes
- Users must have the OpenAI API library for Python installed in order for this program to work. The library can be installed using the following pip command: `pip install openai`
- The program has the API key set as an environment variable by default, the code can however be modified in the following ways so that the user can set up their API key differently:
  - Use a configuration file to store the API key
  - Pass the API key through a command-line argument
  - Use a keyring library
  - Hardcode the API key (not recommended)
- The `openai.Completion.create()` function call includes several parameters that can be adjusted to change the behavior of the chatbot. More information regarding the parameters can be found on [OpenAI's API documentation](https://platform.openai.com/docs/api-reference/completions/create).


## AI Image Generator using OpenAI's DALL-E Model
**[DALLEImageGenerator.py](https://github.com/joshfarias/Python/blob/main/src/DALLEImageGenerator.py)**

This program uses [OpenAI's API](https://openai.com/blog/openai-api) to generate images based on user prompts using OpenAI's DALL-E model. For best results, user prompts should be clear and concise. For example `orange cat` vs `orange cat sitting on a windowsill overlooking a city skyline at sunset, photorealistic`

<div style="display: flex; justify-content: center;">
  <div style="width: 50%;">
    <img src="https://github.com/joshfarias/Python/blob/main/images/orange-cat.png" alt="orange cat" style="width: 50%;">
  </div>
  <div style="width: 50%;">
    <img src="https://github.com/joshfarias/Python/blob/main/images/better-cat-prompt.png" alt="better orange cat prompt" style="width: 50%;">
  </div>
</div>

### Notes
- Users must have the OpenAI API library for Python installed in order for this program to work. The library can be installed using the following pip command: `pip install openai`
- The program has the API key set as an environment variable by default, the code can however be modified in the following ways so that the user can set up their API key differently:
  - Use a configuration file to store the API key
  - Pass the API key through a command-line argument
  - Use a keyring library
  - Hardcode the API key (not recommended)
- By default the program is set to generate a single image with a resolution of `256x256`. This was done for prompt testing purposes due to the greater charges OpenAI places on higher resolution images. This however can easily be changed by modifying the `size` parameter in the `openai.Image.create()` function call to a greater resolution such as `1024x1024` and by modifying the `n` parameter to a set number of how many images you want such as `3`.
