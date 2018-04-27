from generate_data import gen_data
import random

class _music_database:
    def __init__(self):
        self.musics = {}
        self.users = {}
        self.recommend = {}

    def load_database(self, file, user_num):
        self.users, self.musics = gen_data(file, user_num)

    def likes(self, user, music):
        if self.users.has_key(user):
            self.users[user].append(music)
        else:
            self.users[user] = [music]

        if self.musics.has_key(music):
            self.musics[music].append(user)
        else:
            self.musics[music] = [user]

        return {"status": "success"}

    def dislikes(self, user, music):
        if self.users.has_key[user] and self.musics.has_key[music]:
            self.users[user].remove(music)
            self.musics[music].remove(user)
            return {"status": "success"}

    def get_user_musiclist(self, user):
        if self.users.has_key(user):
            d = {"status": "success"}
            d[user] = self.users.get(user)
            return d
        else:
            return {"status": "error", "error": "user doesn't exists"}

    def get_music_fanlist(self, music):
        if self.musics.has_key(music):
            d = {"status": "success"}
            d[music] = self.musics.get(music)
            return d
        else:
            return {"status": "error", "error": "music doesn't exists"}

    def random_user(self):
        user_list = self.users.keys()
        user = user_list[random.randint(0, len(user_list))]
        music_list = self.users.get(user)
        d =  {"user_name": user, "music_list": music_list, "status": "success"}
        return d


if __name__ == "__main__":
    mdb = _music_database()
    mdb.load_database("./data/test_sample.txt", 2000)
    fans = mdb.get_music_fanlist("Dreadlock Holiday")
    print fans
    print fans[user][0]
    print mdb.get_user_music(fans[user][0])
    #print mdb.random_user()