from random import choice


class MusicWorld():
    def __init__(self, genres):
        ''' Dictionary(Genre) '''
        self.genres = genres
        self.money = 0

    def add_artist(self, genre, artist, songs):
        if genre in self.genres.keys():
            self.genres[genre][artist] = songs
        else:
            self.genres[genre] = {artist: songs}

    def add_songs(self, songs):
        for song in songs:
            self.songs.append(song)

    def __str__(self):
        s = ''
        for genre in self.genres:
            s += '\nGenre: {}\nArists:\n'.format(genre)
            for artist in self.genres[genre]:
                s += '{} - {}\n'.format(artist,
                                        ', '.join(self.genres[genre][artist]))
        return s

    def get_song(self, genre):
        artists = self.genres[genre]
        l = []
        for artist in artists.keys():
            songs = artists[artist]
            for song in songs:
                l.append(song)
        return choice(l)

    def my_artists(self, genre):
        return '||'.join(self.genres[genre].keys())

    def is_correct(self, answer, song, genre, money):
        if song in self.genres[genre][answer]:
            self.genres[genre][answer].remove(song)
            self.money += money
            return True
        return False

    def keep_going(self, genre):
        artists = self.genres[genre]
        l = []
        for artist in artists.keys():
            songs = artists[artist]
            for song in songs:
                l.append(song)
        return l

    def get_genres(self):
        return '\n'.join(self.genres.keys())


class MovieWorld():
    def __init__(self, genres):
        ''' Dictionary(Genre) '''
        self.genres = genres
        self.money = 0

    def add_actor(self, genre, actor, movies):
        if genre in self.genres.keys():
            self.genres[genre][actor] = movies
        else:
            self.genres[genre] = {actor: movies}

    def add_movies(self, movies):
        for movie in movies:
            self.movies.append(movie)

    def __str__(self):
        s = ''
        for genre in self.genres:
            s += '\nGenre: {}\nArists:\n'.format(genre)
            for artist in self.genres[genre]:
                s += '{} - {}\n'.format(actor,
                                        ', '.join(self.genres[genre][actor]))
        return s

    def get_movie(self, genre):
        actors = self.genres[genre]
        l = []
        for actor in actors.keys():
            movies = actors[actor]
            for movie in movies:
                l.append(movie)
        return choice(l)

    def my_actor(self, genre):
        return '||'.join(self.genres[genre].keys())

    def is_correct(self, answer, movie, genre, money):
        if movie in self.genres[genre][answer]:
            self.genres[genre][answer].remove(movie)
            self.money += money
            return True
        return False

    def keep_going(self, genre):
        actors = self.genres[genre]
        l = []
        for actor in actors.keys():
            movies = actors[actor]
            for movie in movies:
                l.append(movie)
        return l

    def get_genres(self):
        return '\n'.join(self.genres.keys())
