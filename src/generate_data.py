from generate_name import gen_names
import random

def gen_data(song_file, n_user):
    names = gen_names(n_user)
    with open(song_file) as f:
        songs = open(song_file).readlines()
        songs = songs[0].split('\r')
        songs = songs[:50]

    user_songs = {}
    user_songs = user_songs.fromkeys(names)
    song_users = {}
    song_users = song_users.fromkeys(songs, [])
    print song_users
    for u in user_songs:
        song_list = random.sample(songs, random.randint(1, len(songs)/10))
        user_songs[u] = song_list[:]
        for s in song_list:
            print s,song_users[s]
            song_users[s].append(u)


    return user_songs, song_users


if __name__ == "__main__":
    u_s, s_u = gen_data('./data/test_sample.txt', 20)
#    print s_u
    #for i in s_u:
        #print s_u[i]
#    print len(s_u)
