# importing required APIs
from imdb import IMDb
import imdb


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
# @param list_of_movies--> to avoid the repeated in this list
# @return A list of top 10 recommended movies
def get_recommended(genres: str, list_of_movies: list):
    movie_db = imdb.IMDb()
    top_movies = movie_db.get_top50_movies_by_genres(genres)  # best 50 movies according to the genres
    top_10_movies = []
    number_of_movies = 10
    j = 0
    while j < number_of_movies:
        top_10_movies.append(top_movies[j]['title'])  # best 10 movies according to the genres
        for i in range(len(list_of_movies)):
            if top_movies[j]['title'] == list_of_movies[i]:
                top_10_movies.remove(top_movies[j]['title'])  # best 10 movies according to the genres
                number_of_movies = number_of_movies +1
        j = j + 1
    return top_10_movies


# checks for the most watched genres
# @param list_of_movies: list of watched movies by name
# @return recommended list of movies
# @return list_of_movies --> a helper for ger recommended
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

    return get_recommended(genres[maxIndex], list_of_movies)


if __name__ == '__main__':
    a7a = get_recommended_list(["Avatar: The Way of Water", "avengers", "frozen", "barbie", "showhank"])
    print(a7a)