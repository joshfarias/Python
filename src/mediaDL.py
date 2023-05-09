##############################################################################
# 
#       Program Name: mediaDL.py
#
#       Description: Downloads media from a given URL using the 
#       BeautifulSoup library to send get requests and parse URL for media
#       
#       Language: Python
#
#       Date: 4/11/2023
# 
#       Author: Joshua Farias
#
##############################################################################

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

#function to download a file from a given URL
def download_file(url, folder):
    # Get the filename from the URL
    filename = os.path.basename(urlparse(url).path)
    # Create the full path for the downloaded file
    filepath = os.path.join(folder, filename)
    # Download the file
    response = requests.get(url, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)

#prompt the user to enter the URL of a forum thread
thread_url = input('Enter the URL of a forum thread: ')

#send get request to the thread URL and parse the HTML code
response = requests.get(thread_url)
soup = BeautifulSoup(response.content, 'html.parser') #parse url

#extract the URLs of all media files from the HTML code
media_urls = []
for link in soup.find_all('a'):
    href = link.get('href')
    #searches for JPG, PNG, GIF, WEBM and MP4 media formats
    if href and ('.jpg' in href or '.png' in href or '.gif' in href or '.webm' in href or '.mp4' in href):
        media_url = urljoin(thread_url, href)
        media_urls.append(media_url)

#create a folder to store the downloaded media files
folder = os.path.join(os.getcwd(), 'media')
if not os.path.exists(folder):
    os.makedirs(folder)

#download all media files to the folder
for media_url in media_urls:
    print(f'Downloading {media_url}...')
    download_file(media_url, folder)

print('All media files downloaded!')
