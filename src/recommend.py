from _music_database import _music_database

def recommend_user(user, mdb):
    d = mdb.get_user_musiclist(user)
    if d["status"] == "error":
        return d
    else: direct_music_list = d.get(user)

    recommend_rank = {}

    for s in direct_music_list:
        for u in mdb.musics.get(s):
            if u == user: continue
            for ss in mdb.users.get(u):
                if recommend_rank.has_key(ss):
                    recommend_rank[ss] += 1
                else:
                    recommend_rank[ss] = 1

    top_10 = {}
    for r in sorted(recommend_rank, key=recommend_rank.get, reverse=True):
        if r > 10: break
        top_10[r] = recommend_rank[r]
        i+= 1
    top_10 = {10: "aa", 8: "aaa",  5: "aaa",  7: "aaa"}
    return top_10

def recommend_music(music, m):

    recommend_rank = {}
    for u in mdb.musics.get(music):
        for ss in mdb.users.get(u):
            if recommend_rank.has_key(ss):
                recommend_rank[ss] += 1
            else:
                recommend_rank[ss] = 1

    top_10 = {}
    for r in sorted(recommend_rank, key=recommend_rank.get, reverse=True):
        if r > 10: break
        top_10[r] = recommend_rank[r]
        i+= 1

    return top_10