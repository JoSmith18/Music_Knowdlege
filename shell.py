import core, disk
from random import choice


def play_game(musicworld, song, genre):
    points = 5
    while True:
        answer = valid_name(musicworld, genre)
        if musicworld.is_correct(answer, song, genre, points):
            print('That Is Correct! Keep Going!')
            return None
        print('Sorry You\'re Wrong !!\n')
        points = max(0, points - 2)


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


def main():
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
    print(musicworld.points)


if __name__ == '__main__':
    main()