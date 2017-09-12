import core, disk
from random import choice


def play_game(musicworld, song, genre):
    money = 25
    while True:
        answer = valid_name(musicworld, genre)
        if musicworld.is_correct(answer, song, genre, money):
            print('That Is Correct! Keep Going!')
            return None
        print('Sorry You\'re Wrong !!\n')
        points = max(0, money - 10)


def print_artist(artists):
    for item in artists:
        return '||'.join(artists.keys())


def valid_name(musicworld, genre):
    while True:
        answer = input('Who Made It: {}\n>>>'.format(
            core.MusicWorld.my_artists(musicworld, genre)))
        if answer in musicworld.genres[genre].keys():
            return answer
            break
        else:
            print('Invalid Input!!!!!!\n')


def music_main():
    musicworld = core.MusicWorld({})
    disk.unlock_music(musicworld)
    genres = musicworld.get_genres()
    print(
        'Test Your Rap Knowledge!!\nYou Will Get A Song And Have To Pick The Artist Who Made It!!\n'
    )

    genre = input(
        'What Genre Would You Like To Try:\n{}\n>>> '.format(genres)).title()
    while musicworld.keep_going(genre):
        song = musicworld.get_song(genre)
        print('Your Song Is:{}'.format(song))
        play_game(musicworld, song, genre)
    print(musicworld.money)


def movie_main():
    movieworld = core.MovieWorld({})
    disk.unlock_movies(movieworld)
    genres = movieworld.get_genres()
    print(
        'Test Your Movie Knowledge!!\nYou Will Get A Movie Title And Have To Pick The Actor Who Played In It!!\n'
    )
    genre = input(
        'What Genre Would You Like To Try:\n{}\n>> '.format(genres)).title()
    while movieworld.keep_going(genre):
        movie = movieworld.get_movie(genre)
        print('The Movie Title Is: {}'.format(movie))
        play_game(movieworld, movie, genre)
    print(movieworld.money)


def main():
    while True:
        category = input('Would You Like To Try Movie or Music\n>>> ').title()

        if category == 'Movie'.title():
            movie_main()
            break
        elif category == 'Music'.title():
            music_main()
            break
        else:
            print('Invalid Choice')


if __name__ == '__main__':
    main()