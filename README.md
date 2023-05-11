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

This program uses [OpenAI's API](https://openai.com/blog/openai-api) to generate images based on user prompts using OpenAI's DALL-E model. For best results, user prompts should be clear and concise. For example `cat` vs `orange cat sitting on a windowsill overlooking a city skyline at sunset, photorealistic`:

![Orange Cat](https://github.com/joshfarias/Python/blob/main/images/cat.png) ![Orange Cat Sitting on Windowsill](https://github.com/joshfarias/Python/blob/main/images/better-cat-prompt.png)

### Notes
- Users must have the OpenAI API library for Python installed in order for this program to work. The library can be installed using the following pip command: `pip install openai`
- The program has the API key set as an environment variable by default, the code can however be modified in the following ways so that the user can set up their API key differently:
  - Use a configuration file to store the API key
  - Pass the API key through a command-line argument
  - Use a keyring library
  - Hardcode the API key (not recommended)
- By default the program is set to generate a single image with a resolution of `256x256`. This was done for prompt testing purposes due to the greater charges OpenAI places on higher resolution images. This however can easily be changed by modifying the `size` parameter in the `openai.Image.create()` function call to a greater resolution such as `1024x1024` and by modifying the `n` parameter to a set number of how many images you want such as `3`.


## NBA Player Stats
**[NBAPlayerStats.py](https://github.com/joshfarias/Python/blob/main/src/NBAPlayerStats.py)**

This program uses swar's [NBA API](https://github.com/swar/nba_api) to fetch career, season and game log stats for a given NBA player that the program prompts the user to enter. Here is an example of the program running using the NBA Player Luka Doncic:

### Carrer Stats:
![Career Stats](https://i.imgur.com/o2gVNH5.png)

### Season Stats:
![Season Stats](https://i.imgur.com/vxIyLvF.png)

### Game Log Stats:
![](https://i.imgur.com/7esLd5m.png)

### Notes
- Users must have the `nba_api` and `tabulate` libraries for Python installed in order for this program to work. The libraries can be installed using the following pip command: `pip install nba_api tabulate`

## CircuitPython RP2040 Projects using Adafruit's HID Library

This project is based on the following GitHub Repo:

https://github.com/dbisu/pico-ducky

The payload was created by SurfKahuna (RJC)

The payload targets Windows computers. First it opens up Notepad using Run and draws Bart Simpson in ASCII characters then writes the message: "I will learn to lock my computer." several times before locking the computer.

[Project Repo](https://github.com/joshfarias/Pico/tree/main/src/circuitPython/HID)

### Steps:

  - Download the latest [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) firmware and the [Adafruit HID library](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases), you should have a `.UF2` file and a `.ZIP` file.
  - Connect the Raspberry Pi Pico (RP2040) to computer using USB-A to Micro-USB cable.
  - Put the Pico into bootloader mode by holding down the BOOTSEL button when plugging in the USB.
  - The Pico should appear as a mass storage device.
  - Move the `.UF2` firmware file that was downloaded from Circuit Python's [website](https://circuitpython.org/board/raspberry_pi_pico/) on to the Pico.
  - The Pico should now appear as `CIRCUITPY`
  - Extract the contents of the `.ZIP` file that was downloaded from [Adafruit HID library](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases) and  search for the following folder:
    - `/adafruit_hid`
  - Select `adafruit_hid` and copy it into the `lib` folder in `CIRCUITPY`
  - To make a copy of this project you can overwritte the contents of the `payload.dd` and `code.py` file with the code from this repo. Just be forewarned as the code will automatically run upon plugging in the Pico. [`code.py`](https://github.com/dbisu/pico-ducky/blob/main/duckyinpython.py) is a Python script that converts DuckyScript into MicroPython code for Pico. The `payload.dd` file is a binary file that contains the keystrokes and other actions that will be executed by the Pico when it is plugged in.

## Media Downloader

**[mediaDL.py](https://github.com/joshfarias/Python/blob/main/src/mediaDL.py)**

This program uses the `BeautifulSoup` and `requests` Python libraries to parse through a given URL from a web forum and extract and download media that is in the form of (.JPG, .PNG, .GIF, .WEBM and .MP4). Here is an example of the program running:

![Media Downloader](https://i.imgur.com/Ewf7OA0.png)

The media that is downloaded will be saved within a folder entitled `media` within the directory the program is in.

### Notes:

  - Users must have the `BeautifulSoup` and `requests` libraries for Python installed in order for this program to work. The libraries can be installed using the following pip command: 
    `pip install beautifulsoup4 requests`
