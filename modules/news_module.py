import webbrowser

import requests

import voice_assistant as assistant

main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=56aa0db700534f95ba5234774b1dbd1c'
main_page = requests.get(main_url).json()
articles = main_page['articles']

day = ['first', 'second', 'third', 'fourth', 'fifth']

def get_news():
    headlines = []
    for article in articles:
        headlines.append(article['title'])
    assistant.speak('Today\'s top 5 Headlines are:')
    for i in range(len(day)):
        assistant.speak(f'{day[i]} headline: {headlines[i]}')

def get_specific_news(response):
    global content
    try:
        for i in range(len(day)):
            if day[i] in response:
                content = articles[i]['description']
                assistant.speak(content)
                assistant.speak('Do you wish to know more about it?')
                resp = assistant.takeCommand().lower()
                if 'yes' in resp or 'yeah' in resp or 'yup' in resp:
                    assistant.speak('Opening news on browser')
                    webbrowser.open(articles[i]['url'])
        if content is None:
            assistant.speak('No more information on this.')
    except:
        assistant.speak('No more information on this.')

