import json


def load_json_library(songs_dict):
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
        user_input = user_input_ckeck()
        user_checked_songs = [full_list[number-1] for number in user_input]
        return [songs_dict[i[0]][i[1]] for i in user_checked_songs]


def user_input_ckeck(look_for:str,range_u:int):
    if look_for == 'songs':
        user_input = input('Please type numbers of the songs you want to remove: ')
        if ''.join(user_input.split()).isnumeric():
            user_input = [int(i)-1 for i in user_input]
            check = [i in range(range_u) for i in user_input]
            if all(check):
                return user_input
            else:
                print('Make sure you typed correct numbers.')
                return user_input_ckeck(look_for,range_u)
    if look_for == 'playlist':
        user_input = input('Please type the number of playlist you want to modify: ')
        if user_input.isnumeric() and int(user_input) in range(1, range_u+1):
            return int(user_input.strip()) -1
        else:
            print('Please, type again.')
            user_input_ckeck(look_for, range_u)
    
user_input_ckeck('playlist', 2)
