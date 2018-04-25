from generate_name import gen_names
import random

def gen_data(song_file, n_user):
    names = gen_names(n_user)
    with open(song_file) as f:
        songs = open(song_file).readlines()
        songs = songs[0].split('\r')

    user_songs = {}
    user_songs = user_songs.fromkeys(names)
    song_users = {}
    #song_users = song_users.fromkeys(songs, [])
    #print song_users
    for u in user_songs:
        song_list = random.sample(songs, random.randint(1, len(songs)/10))
        user_songs[u] = song_list[:]
        #print user_songs
        for s in song_list:
            if s not in song_users:
                song_users[s]=[u]
            else:
                song_users[s].append(u)
            '''if u not in song_users[s]:
                print u
                song_users[s].append(u)'''
            #print s,song_users[s]


    return user_songs, song_users


if __name__ == "__main__":
    u_s, s_u = gen_data('./data/test_sample.txt', 2000)
#    print s_u
    '''for i in s_u:
        print s_u[i]'''
#    print len(s_u)
