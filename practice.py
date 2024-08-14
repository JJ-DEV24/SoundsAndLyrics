"""Requests"""

# Install requests libray -- pip install requests
# Grab URL, see below

import requests
import os

'''Make a request to Pedro's 'Full Stack Portfolio' website'''
# r = requests.get('https://fullstackportfolio.me/')
# print(r)
# # prints <Response [200]>
# print(r.text)
# prints the content of the response in unicode. Content is in html but can be parsed if you need to manipulate the
# text.

from bs4 import BeautifulSoup

# def parse_lyrics(response):
#     soup = BeautifulSoup(response.text, "html.parser")
#     retrieved_lyrics = soup.find_all(attrs={"data-lyrics-container": "true"})
#     answer = []
#     for lyrics in retrieved_lyrics:
#         answer.append(str(lyrics.text))
#     return ''.join(answer)
#
#
# if os.path.isfile('lyrics.html'):
#     with open('lyrics.html', 'r') as f:
#         print('Opening saved file')
#         read_lyrics = f.read()
#         print(read_lyrics)
# else:
#     print('Retrieving lyrics')
#     response = requests.get('https://genius.com/Kaytranada-do-2-me-lyrics')
#     lyrics = parse_lyrics(response)
#     with open('lyrics.html', 'w', encoding="utf-8") as f:
#         f.write(lyrics)
#         print(lyrics)


# """Get lyrics to GloRilla - Yeah Glo!"""
#
# import requests
# from bs4 import BeautifulSoup
#
# def get_lyrics(response):
#     soup = BeautifulSoup(response.text, "html.parser")
#     retrieved_lyrics = soup.find_all(attrs={"data-lyrics-container": "true"})
#     answer = []
#     for lyrics in retrieved_lyrics:
#         answer.append(str(lyrics.text))
#     return ''.join(answer)
#
# if os.path.isfile('glorilla_yeah_glo.html'):
#     with open('glorilla_yeah_glo.html', 'r') as f:
#         read_lyrics = f.read()
#         print(read_lyrics)
# else:
#     response = requests.get('https://genius.com/Glorilla-yeah-glo-lyrics')
#     lyrics = get_lyrics(response)
#     with open('glorilla_yeah_glo.html', 'w',encoding="utf-8") as f:
#         f.write(lyrics)
#         print(lyrics)
#
#
# for item in os.listdir():
#     print(item)
# if os.path.isfile('rihanna-disturbia-lyrics'):
#     print('This file exists.')
# else:
#     print('This file does not exist')
#

#
# if os.path.isdir(r'C:\Users\jtjos\Desktop'):
#     for each in os.listdir():
#         print(each)
# else:
#     print('The Desktop directory does not exist.')

# try:
#     with open('WWW.py', 'r') as f:
#         print(f.read())
#
# except FileExistsError:
#     print('This file does not exist')


with open('my-brand-new-file', 'r'):
    print('this file exists')
'''Directories in OS Module'''

# print(os.getcwd())
# os.chdir(r'C:\Users\jtjos\PycharmProjects')
# print(os.getcwd())
# os.chdir(r'C:\Users\jtjos')
# print(os.getcwd())
# os.chdir(r'C:\Users\jtjos\Desktop')
# print(os.getcwd())
#
# for each in os.listdir():
#     print(each)


# os.chdir(r'C:\Users\jtjos\PycharmProjects')
# print(os.getcwd())
# for each in os.listdir():
#     print(each)
#
# os.chdir(r'C:\Users\jtjos\PycharmProjects\SoundsAndLyrics')
# for each in os.listdir():
#     print(each)
#






# response = requests.get('https://genius.com/Kaytranada-do-2-me-lyrics')
#
# lyrics = parse_lyrics(response)
# print(lyrics)


#
# if os.path.isfile('pedros_website.html'):
#      with open('pedros_website.html', 'r') as f:
#           read_lyrics = f.read()
#           print(read_lyrics)

# else:
# r = requests.get('https://fullstackportfolio.me/')
# with open('pedros_website.html', 'w') as f:
#      f.write(r.text)
# print('File created')

'''
if the file exists, open and read from the file

if the file does not exist, 
'''

# except FileExistsError as e:
#      print('This file already exists')
# finally:
#      f.close()
#      print('This file is closed')


# '''Get Pedro's avatar and save it to a file'''
# r_image = requests.get('<path d="M264 0H0V280H264V0Z" fill="#2C1B18"></path>')
