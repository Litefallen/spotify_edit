import json


def load_json_library(songs_dict): # displaying list with all songs in playlist/library, return ids of the songs to remove
        o_artist_list = sorted(songs_dict.keys(), key=lambda x: x.lower())
        full_list = []
        for artist in o_artist_list:
            if len(songs_dict[artist]) > 1:
                for song in songs_dict[artist]:
                    full_list.append((artist,song))
            else:
                full_list.append((artist,tuple(songs_dict[artist].keys())[0]))

        for i in enumerate(full_list, start=1):
            print(f"{i[0]}. {i[1][0]} - {i[1][1]}")
        user_input = user_input_ckeck(look_for='songs', range_u=len(full_list))
        # print(user_input)
        user_checked_songs = [full_list[number] for number in user_input]
        return [songs_dict[i[0]][i[1]] for i in user_checked_songs]


def user_input_ckeck(look_for:str,range_u:int):
    if look_for == 'fav_or_pl': # errorcheck for choosing what to edit, favorites or playlist
        user_input = input('Please type 1 if you want to modify one of your playlists\nor type 2 to modify your favorites: ')
        if user_input.isnumeric() and int(user_input) in range(1, range_u+1):
            return int(user_input.strip())
        else:
            print('Please, type again.')
            user_input_ckeck(look_for, range_u)
    if look_for == 'songs': # errorcheck for songs removal
        user_input = input('Please type numbers of the songs you want to remove: ').split(' ')
        final_input = []
        for num in user_input:
            if num.isnumeric():
                user_input = int(num)-1
            else:
                print('Make sure you typed correct numbers.')
                return user_input_ckeck('songs',range_u)
            if user_input in range(range_u):
                final_input.append(user_input)
            else:
                print('Make sure you typed correct numbers.')
                return user_input_ckeck(look_for,range_u)
    if look_for == 'playlist': #errorcheck for playlist choosing
        user_input = input('Please type the number of playlist you want to modify: ')
        if user_input.isnumeric() and int(user_input) in range(1, range_u+1):
            return int(user_input.strip()) -1
        else:
            print('Please, type again.')
            user_input_ckeck(look_for, range_u)
    return final_input
    
    