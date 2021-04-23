import os
import time
from os import path as pathfinder
import random

import voice_assistant as assistant
from modules.search_module import search_google

movie_dir = 'S:\Movies and Shows\Movies'
movies = []

def add_movies(moviepath):
    items = os.listdir(moviepath)
    # print(len(items))
    movie_folders = []
    for item in items:
        path = os.path.join(moviepath, item)
        # If mp4 file, add to movies
        if pathfinder.isfile(path) and ('.mp4' in path or '.mkv' in path):
            # print('Adding to movies')
            movies.append(path)
        # If movie folder, add to folders list
        elif pathfinder.isdir(path):
            # print('Adding to movie folders')
            movie_folders.append(path)

    # Parse all folders and repeate above steps
    for folder_path in movie_folders:
        # print(folder_path)
        add_movies(folder_path)


def play_movie():
    add_movies(movie_dir)
    n = random.randint(0, len(movies)-1)
    # print(n)
    print(movies[n])
    os.startfile(movies[n])
    time.sleep(10)

def run_movie(command):
    print('User: ' + command)
    like_movie = False
    if 'surprise me' in command or 'you pick one' in command or 'choose' in command or 'you pick' in command or\
            'you pic' in command:
        assistant.speak('Playing my favorite movie.')
        play_movie()
        while like_movie is False:
            assistant.speak('Do you like it?')
            command = assistant.takeCommand()
            if 'no' in command or 'change movie' in command or 'pick a different movie' in command or\
                    'change the movie' in command:
                assistant.speak('Playing a different movie.')
                play_movie()
            elif 'yes' in command or 'thank you' in command or 'thankyou' in command:
                like_movie = True
                assistant.speak('Enjoy the movie sir.')
    else:
        if 'none' in command or command is None:
            assistant.speak('I did not get you. Please repeat the movie name')
            command = assistant.takeCommand()
            run_movie(command)
        else:
            search_google(command + ' watch online')


# if __name__ == "__main__":
#     get_movie()