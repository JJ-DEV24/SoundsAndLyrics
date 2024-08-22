"""                                      Sounds and Lyrics

This application will give the user the ability to search for lyrics to a song and play it. The user
can sing along as the lyrics are highlighted because they are synced to the song

Pages on web application:

- Home page
    - Introduction to the web application and an explanation of how to use and navigate it.
    - Search bar at the top of the page. User can search for keywords such as artist, song title and lyrics

- About page
    - Search bar at the top of the page
    - Brief explanation of when application was built, why it was built, and developmental goals for the future

- Artists
    - A - Z directory of artists. Search bar at the top of the page

- Recent searches/ history
    - List of recent searches. Includes artist's name, song title and date when searched

- Lyrics page
    - Displays artist's name, title of the song and lyrics.
    - Provides information about the song such as release date, name of album, credits and length of song
    - Gives the user the option to play the song if they want to sing along
    - Highlight each word/ line of lyrics and synchronise it with the song (e.g. Spotify/ Amazon music)

Colour scheme:

- Pink, red, white, green & blue
- Fun, colourful,
"""
import os.path
from pathlib import Path
import os

"""Import templates"""
from typing import Union
from fastapi import FastAPI
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup

app = FastAPI()
templates = Jinja2Templates(directory="html")
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


# url_endpoints = ["home", "top_5", "artists"]
url_endpoints = {
    "home": {"name": "home", "icon": "🏠", "url": "home"}, 
    "top5": {"name": "top 5", "icon": "🧐", "url": "top_5"}, 
    "artists": {"name": "artists", "icon": "🎤", "url": "artists"}  
}


"""Home page"""

"""Original path passed as argument through app.get decorator to retrieve content from homepage.html"""


@app.get('/', response_class=HTMLResponse)
def index_page(request: Request):
    return templates.TemplateResponse(request=request, name="s_and_l_index.html", context={"nav": url_endpoints})

@app.get('/home', response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="s_and_l_index.html", context={"nav": url_endpoints})

@app.get('/top_5', response_class=HTMLResponse)
def top_5_page(request: Request):
    return templates.TemplateResponse(request=request, name="this_weeks_top_5_tracks.html", context={"nav": url_endpoints})

@app.get('/artists', response_class=HTMLResponse)
def artists_page(request: Request):
    return templates.TemplateResponse(request=request, name="artists.html", context={"nav": url_endpoints})


@app.post('/get-lyrics')
async def get_lyrics(request: Request):
    user_data = await request.form()
    user_data_a_n = user_data['artists_name'].split(' ')
    user_data_t = user_data['title'].split(' ')
    artists_name = '-'.join(user_data_a_n)
    title = '-'.join(user_data_t)
    the_current_path = str(Path.cwd())
    path_to_lyrics = f'{the_current_path}\\retrieved_lyrics\\{artists_name}-{title}-lyrics.html'
    if os.path.isfile(path_to_lyrics):
        return templates.TemplateResponse(request=request, name="get_lyrics.html", context={"retrieved_lyrics": read_lyrics(path_to_lyrics), "nav": url_endpoints})

    else:
        artists_name_split = (user_data['artists_name'].split(' '))
        title_split = (user_data['title'].split(' '))
        artists_name_joined,title_joined = format_artists_and_title(artists_name_split, title_split)
        request_lyrics(artists_name_joined, title_joined, path_to_lyrics)
    # return read_lyrics(path_to_lyrics)
    return templates.TemplateResponse(request=request, name="get_lyrics.html", context={"retrieved_lyrics": read_lyrics(path_to_lyrics), "nav": url_endpoints})



def request_lyrics(artist, title, filepath):
    with open(filepath, 'w', encoding="utf-8") as f:
        response = requests.get(f'https://genius.com/{artist}-{title}-lyrics')
        soup = BeautifulSoup(response.text, "html.parser")
        retrieved_lyrics = soup.find_all(attrs={"data-lyrics-container": "true"})
        answer = []
        for lyrics in retrieved_lyrics:
            answer.append(str(lyrics.text))
        f.write(str(" ".join(answer)))


def read_lyrics(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        lyrics = f.read().replace("\\", " ")
    return lyrics
    


def format_artists_and_title(split_list_of_artists, split_list_of_title):
    joined_artists = '-'.join(split_list_of_artists)
    joined_title = '-'.join(split_list_of_title)
    return joined_artists, joined_title







"""About page"""


@app.get('/aboutpage', response_class=HTMLResponse)
def about_page(request: Request):
    return templates.TemplateResponse(request=request, name="aboutpage.html")


"""Artists"""
artists = ['Beyonce', 'Rihanna', 'Justin Timberlake']


@app.get("/artists")
def get_artists():
    return f"These artists are headlining tonight: {artists[0]}, {artists[1]} and {artists[2]}."


"""Rihanna, Disturbia"""


def get_rihanna_disturbia_lyrics():
    response = requests.get('https://genius.com/Rihanna-disturbia-lyrics')
    soup = BeautifulSoup(response.content, "html.parser")
    r_d_lyrics_extracted = soup.find_all(attrs={"data-lyrics-container": "true"})
    answer = []
    for lyrics in r_d_lyrics_extracted:
        answer.append(str(lyrics.text))
    return answer


@app.get('/rihanna_disturbia_lyrics', response_class=HTMLResponse)
def rihanna_disturbia_lyrics_page(request: Request):
    return templates.TemplateResponse(request=request, name="rihanna_disturbia_lyrics.html",
                                      context={"v": get_rihanna_disturbia_lyrics(),
                                               "Jess": "jessica tendai daphne joseph"})


"""Beyonce"""
beyonce = ["Halo", "Super power", "Bodyguard"]


@app.get('/beyonce', response_class=HTMLResponse)
def get_beyonce(request: Request):
    return templates.TemplateResponse(request=request, name="beyonce.html", context={"beyonce": beyonce})


@app.get("/beyonce_ya_ya_lyrics")
def read_root():
    response = requests.get("https://genius.com/Beyonce-ya-ya-lyrics")
    html = BeautifulSoup(response.text)
    html.find("Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
    return html.find("div", {"class": "Lyrics__Container-sc-1ynbvzw-1 kUgSbL"}).text
