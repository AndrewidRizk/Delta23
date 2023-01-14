from string import punctuation
from flask import Flask, render_template, request, url_for, redirect
import string
import os, sys
import json




userdata = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'userdata.json')
#userdata = "userdata.json"



import requests
def find_trailer(name):

    api_key = "AIzaSyAyyf9lHMVXY5q4aFNIo4BTd8UVRJkTjo4"

    movie_name = "name"

    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie_name}+trailer&type=video&key={api_key}"

    response = requests.get(search_url)

    data = response.json()

    if data["items"]:
        video_id = data["items"][0]["id"]["videoId"]
        link = "https://www.youtube.com/watch?v="+video_id
        #print(link)
    else:
        print("No video found.")

    return link


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
    return [len(movies)] + [username] + movies

def postMovie(user, movie):
    if movie == "":
        return
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

## just username -> movies for now
def driver(username, new_movie):
    toPost = []
    toPost = getAuth(username)
    return toPost

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST', 'GET'])
def result():
    inp = request.form.to_dict()
    text = inp['text']
    s = driver(text, "")
    return render_template("index.html", text=text, data=s)


@app.route("/add", methods=['POST', 'GET'])
def add():
    inp = request.form.to_dict()
    text = inp['text']
    s = postMovie("example_user", text )
    return render_template("index.html", text=text, data2=s)

if __name__ == '__main__':
    app.run(debug=True, port=5001)