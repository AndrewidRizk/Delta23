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

a = find_trailer("Inside out")
print(a)