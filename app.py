from string import punctuation
from flask import Flask, render_template, request, url_for, redirect
import string
import os, sys
import json
#userdata = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'userdata.json')
userdata = "userdata.json"


def getAuth(username):
    movies = []
    try:
        with open(userdata, 'r') as fh:
            data = json.load(fh)
            for user in data['users']:
                if user['id'] == username:
                    movies = user['movies']
    except FileNotFoundError:
        print("The file userdata.json was not found.")
    except json.decoder.JSONDecodeError:
        print("The file userdata.json is not well-formatted.")
    except KeyError:
        print("The field 'users' or 'id' or 'movies' is not in the json file.")
    return movies

def postMovie(user, movie):
    with open(userdata, "r") as fh:
        data = json.load(fh)

    user_exists = False
    for user in data['users']:
        if user['id'] == user:
            user_exists = True
            user['movies'].append(movie)
            break
    if not user_exists:
        data['users'].append({'id': user, 'movies': [movie]})
    
    with open(userdata, 'w') as fh:
        json.dump(data, fh)



user_id = 'example_user'
print(getAuth(user_id))