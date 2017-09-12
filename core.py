from random import choice


class MusicWorld():
    def __init__(self, genres):
        ''' Dictionary(Genre) '''
        self.genres = genres
        self.points = 0

    def add_artist(self, genre, artist, songs):
        if genre in self.genres.keys():
            self.genres[genre][artist] = songs
        else:
            self.genres[genre] = {artist: songs}

    def add_songs(self, songs):
        for song in songs:
            self.songs.append(song)

    # def __repr__(self):
    #     return 'Genre:{}(Artist:{}, Songs:{})'.format(self.genre, self.artist,
    #                                                   self.songs)

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

    def is_correct(self, answer, song, genre, points):
        if song in self.genres[genre][answer]:
            self.genres[genre][answer].remove(song)
            self.points += points
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
