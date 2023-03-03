<h1>
  <img src="https://github.com/joshfarias/Python/raw/main/images/python-logo.png" alt="python logo" height="100">
 </h1>

# **Python Programming Projects:**

## Chatbot using text-davinci-003 Model from OpenAI
**[davinci-003-chatbot.py](https://github.com/joshfarias/Python/blob/main/src/davinci-003-chatbot.py)**
This program uses OpenAI's [API](https://openai.com/blog/openai-api) to generate responses to user prompts and questions in an interactive chatbot format. The responses generated are based on OpenAI's text-davinci-003 language model.

Below is an screenshot containing the a brief conversation with the chatbot:

<h1>
<img src="https://github.com/joshfarias/Python/blob/main/images/davinci-003-chatbot.png" alt="python logo" height="75">
</h1>

###### Notes
[^1]: Users must have the OpenAI API library for Python installed in order for this program to work. The library can be installed using the following pip command: `pip install openai`
[^2]: The program has the API key set as an environment variable by default, the code can however be modified in the following ways so that the user can set up their API key differently:
- Use a configuration file to store the API key
- Pass the API key through a command-line argument
- Use a keyring library
- Hardcode the API key (not recommended)
[^3]: The `openai.Completion.create()` function call includes several parameters that can be adjusted to change the behavior of the chatbot. More information regarding the parameters can be found on [OpenAI's API documentation](https://platform.openai.com/docs/api-reference/completions/create).
