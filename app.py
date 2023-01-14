from string import punctuation
from flask import Flask, render_template, request, url_for, redirect
import string
import os, sys
import json



userdata = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'userdata.json')
#userdata = "userdata.json"



def driver(username, new_movie):
    toPost = [[],[]]


def getAuth(username):
    movies = []
    try:
        with open(userdata, 'r') as fh:
            data = json.load(fh)
            user_exists = False
            for user in data['users']:
                if user['id'] == username:
                    user_exists = True
                    movies = user['movies']
                    break
            if not user_exists:
                data['users'].append({'id': username, 'movies': []})
                with open(userdata, 'w') as jsonfile:
                    json.dump(data, jsonfile, indent=4)
                



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
        ## User doesnt exists handled in getAuth
    # if not user_exists:
    #     data['users'].append({'id': user, 'movies': [movie]})
    
    with open(userdata, 'w') as fh:
        json.dump(data, fh, indent=4)



# user_id = 'example_user'
# print(getAuth(user_id))