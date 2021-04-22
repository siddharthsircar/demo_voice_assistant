import webbrowser

import requests

import jarvis_voice_assistant as jarvis

main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=56aa0db700534f95ba5234774b1dbd1c'
main_page = requests.get(main_url).json()
articles = main_page['articles']

day = ['first', 'second', 'third', 'fourth', 'fifth']

def get_news():
    headlines = []
    for article in articles:
        headlines.append(article['title'])
    jarvis.speak('Today\'s top 5 Headlines are:')
    for i in range(len(day)):
        jarvis.speak(f'{day[i]} headline: {headlines[i]}')

def get_specific_news(response):
    global content
    try:
        for i in range(len(day)):
            if day[i] in response:
                content = articles[i]['description']
                jarvis.speak(content)
                jarvis.speak('Do you wish to know more about it?')
                resp = jarvis.takeCommand().lower()
                if 'yes' in resp or 'yeah' in resp or 'yup' in resp:
                    jarvis.speak('Opening news on browser')
                    webbrowser.open(articles[i]['url'])
        if content is None:
            jarvis.speak('No more information on this.')
    except:
        jarvis.speak('No more information on this.')

