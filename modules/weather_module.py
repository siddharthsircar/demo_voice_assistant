import requests
import jarvis_voice_assistant as jarvis

from bs4 import BeautifulSoup

def get_weather():
    try:
        search = 'temperature in delhi'
        url = f'https://www.google.com/search?q={search}'
        req = requests.get(url)
        data = BeautifulSoup(req.text, 'html.parser')
        temp = data.find('div', class_='BNeawe').text
        jarvis.speak(f'Current {search} is {temp}')
    except:
        jarvis.speak('Unable to connect to satellite')