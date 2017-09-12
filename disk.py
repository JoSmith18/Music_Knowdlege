import core


def unlock_music(musicworld):
    with open('music.txt', 'r') as file:
        file.readline()
        artist_info = file.readlines()

    artist_info = list(map(lambda i: i.split('-'), artist_info))
    for genre, artist, songs in artist_info:
        songs = songs.strip().split(', ')
        musicworld.add_artist(genre.strip(), artist.strip(), songs)
