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


Colour scheme:

- Pink, red, white, green & blue
- Fun, energising,
"""

"""Import templates"""
# URL = http://127.0.0.1:8000
# Server = python -m uvicorn main:app --reload
from typing import Union
from fastapi import FastAPI
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup

app = FastAPI()
templates = Jinja2Templates(directory="templates")

"""Original path"""


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}


"""Home page"""

"""Original path passed as argument through app.get decorator to retrieve content from homepage.html"""


@app.get('/', response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="homepage.html")


@app.post('/get-lyrics')
async def get_lyrics(request: Request):
    user_data = await request.form()
    len_artists_name = (user_data['artists_name'].split(' '))
    len_title = (user_data['title'].split(' '))
    if len(len_artists_name) and len(len_title) == 1:
        artists_name = '-'.join(len_artists_name)
        title = '-'.join(len_title)
        response = requests.get(f'https://genius.com/{artists_name}-{title}-lyrics')
        soup = BeautifulSoup(response.text, "html.parser")
        retrieved_lyrics = soup.find_all(attrs={"data-lyrics-container": "true"})
        answer = []
        for lyrics in retrieved_lyrics:
            answer.append(str(lyrics.text))
        return answer

    else:
        if len(len_artists_name) and len(len_title) >= 2:
            artists_name = '-'.join(len_artists_name)
            title = '-'.join(len_title)
            response = requests.get(f'https://genius.com/{artists_name}-{title}-lyrics')
            soup = BeautifulSoup(response.text, "html.parser")
            retrieved_lyrics = soup.find_all(attrs={"data-lyrics-container": "true"})
            answer = []
            for lyrics in retrieved_lyrics:
                answer.append(str(lyrics.text))
            return answer







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
