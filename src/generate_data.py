from generate_name import gen_names
import random

def gen_data(song_file, n):
    names = gen_names(n)
    with open(song_file) as f:
        songs = open(song_file).readlines()
        songs = songs[0].split('\r')

    user_songs = {}
    user_songs = user_songs.fromkeys(names)
    for u in user_songs:
        song_list = random.sample(songs, random.randint(1, len(songs)/10))
        user_songs[u] = song_list

    return user_songs


if __name__ == "__main__":
    d = gen_data('./data/test_sample.txt', 20)
    for i in d:
        print d[i]
