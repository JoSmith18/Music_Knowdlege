import core


def unlock_music(musicworld):
    with open('music.txt', 'r') as file:
        file.readline()
        artist_info = file.readlines()

    artist_info = list(map(lambda i: i.split('-'), artist_info))
    for genre, artist, songs in artist_info:
        songs = songs.strip().split(', ')
        musicworld.add_artist(genre.strip(), artist.strip(), songs)


def unlock_movies(movieworld):
    with open('movie.txt', 'r') as file:
        file.readline()
        actor_info = file.readlines()

    actor_info = list(map(lambda i: i.split('-'), actor_info))
    for genre, actor, movies in actor_info:
        movies = movies.strip().split(', ')
        movieworld.add_actor(genre.strip(), actor.strip(), movies)
