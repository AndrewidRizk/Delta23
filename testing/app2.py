
from string import punctuation
from flask import Flask, render_template, request, url_for, redirect
import string
import os, sys
import json
import requests
# importing required APIs
from imdb import IMDb
import imdb





userdata = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'userdata.json')
#userdata = "userdata.json"




# given the name of the movie, gives the genres (category) of the movie
# @param name_of_the_movie --> takes the name of the movie
# @return Genres of the movie name given
def get_genres(name_of_the_movie: str):
    movie_db = IMDb()  # Data Base of IMDb
    movies = movie_db.search_movie(name_of_the_movie)  # A list of all the movies for this name
    movie = movies[0]  # Get the first movie in the list
    movie_db.update(movie)
    genres = movie['genres']  # Get the Genres

    return genres[0]


# given the genres, generate a list of recommendations
# @param genres --> takes the genres
# @return A list of top 10 recommended movies
def get_recommended(genres: str):
    movie_db = imdb.IMDb()
    top_movies = movie_db.get_top50_movies_by_genres(genres)  # best 50 movies according to the genres
    top_10_movies = []
    for j in range(10):
        top_10_movies.append(top_movies[j]['title'])  # best 10 movies according to the genres

    return top_10_movies


# checks for the most watched genres
# @param list_of_movies: list of watched movies by name
# @return recommended list of movies
def get_recommended_list(list_of_movies):
    genre_list = []
    genres = ['Comedy', 'Romance', 'Drama', 'Animation', 'SCI-FI', 'Action',
              'Mystery', 'Adventure', 'Horror', 'Crime',
              'Fantasy', 'SuperHero']
    number_of_appearances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maxAppearance = 0
    maxIndex = 0

    for z in range(len(list_of_movies)):
        genre_list.append(get_genres(list_of_movies[z]))

    # updating number of appearance of each genre
    for y in genre_list:
        for x in range(12):
            if y == genres[x]:
                number_of_appearances[x] = number_of_appearances[x] + 1
                if number_of_appearances[x] > maxAppearance:
                    maxAppearance = number_of_appearances[x]
                    maxIndex = x

    return get_recommended(genres[maxIndex])


if __name__ == '__main__':
    a7a = get_recommended_list(["kung fu panda"])
    print(a7a)



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
    first = movies[0]
    return [len(movies)] +  movies

def postMovie(user, movie):
    if movie == "":
        return
    with open(userdata, "r") as fh:
        data = json.load(fh)

    for i in data['users']:
        if i["id"] == user:
            if movie in i["movies"]:
                return
            else:
                i["movies"].append(movie)

    # write the updated data back to the json file
    with open(userdata, "w") as f:
        json.dump(data, f, indent = 4)



# user_id = 'example_user'
# print(getAuth(user_id))

## just username -> movies for now
def driver(username, new_movie):
    toPost = []
    toPost = getAuth(username)
    #toRec = get_recommended_list(toPost)
    return toPost



app = Flask(__name__)
 

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_watchlist", methods=['POST', 'GET'])
def result():
    inp = request.form.to_dict()
    text = inp['text']
    s = driver(text, "")
    return render_template("index.html", text=text, data=s, userid = text)


@app.route("/add_movie", methods=['POST', 'GET'])
def add():
    inp = request.form.to_dict()
    text = inp['movie']
    s = postMovie("example_user", text )
    return render_template("index.html", text=text, data2=s)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

