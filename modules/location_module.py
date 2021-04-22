import requests

import jarvis_voice_assistant as jarvis


def get_current_location():
    jarvis.speak('checking sir')
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        url = (f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json')
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        print(geo_data)
        city = geo_data['city']
        country = geo_data['country']
        region = geo_data['region']
        latitude = geo_data['latitude']
        longitude = geo_data['longitude']
        jarvis.speak(f'I believe we are in a city named {city} in {country}')
        jarvis.speak(f'It is the {region}. Longitude: {longitude}, Latitude: {latitude}')
    except Exception as e:
        jarvis.Speak('Sorry, due to network issues could not find current location.')
        pass

