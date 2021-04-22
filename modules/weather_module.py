import requests
import voice_assistant as assistant

from bs4 import BeautifulSoup

def get_weather():
    try:
        search = 'temperature in delhi'
        url = f'https://www.google.com/search?q={search}'
        req = requests.get(url)
        data = BeautifulSoup(req.text, 'html.parser')
        temp = data.find('div', class_='BNeawe').text
        assistant.speak(f'Current {search} is {temp}')
    except:
        assistant.speak('Unable to connect to satellite')