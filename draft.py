import json

def load_json_library():
    with open('artists_songs.json', 'r') as f:
        artist_dict = json.load(f)
        o_artist_list = sorted(artist_dict.keys(), key=lambda x: x.lower())
        full_list = []
        for artist in o_artist_list:
            if len(artist_dict[artist]) > 1:
                for song in artist_dict[artist]:
                    full_list.append((artist,song))
            else:
                full_list.append((artist,tuple(artist_dict[artist].keys())[0]))

    for i in enumerate(full_list, start=1):
        print(f"{i[0]}. {i[1][0]} - {i[1][1]}")
        
# tracks_to_remove = input('Please, type the numbers of the songs you want to delete.\nUse space to separate songs numbers.')
# print(''.join(tracks_to_remove.split()))
# print(tracks_to_remove)
# print(artist_dict[full_list[2][1]])


 # delete fav tracks
    # tracks_to_delete = {"ids": ["2EmZQLQIFm6btRF1TXLchE"]}
    # req = requests.delete(f'https://api.spotify.com/v1/me/tracks', headers=headers, json=tracks_to_delete)


def user_input_ckeck(look_for:str,range_u:int):
    if look_for == 'songs':
        user_input = input('Please type numbers of the songs you want to remove: ').split(' ')
        input_list = []
        input_list.extend(user_input)

        final_input = []
        for num in user_input:
            if num.isnumeric():
                user_input = int(num)-1
            else:
                print('Make sure you typed correct numbers.')
                return user_input_ckeck('songs',33)
            if user_input in range(range_u):
                final_input.append(user_input)
            else:
                print('Make sure you typed correct numbers.')
                return user_input_ckeck(look_for,range_u)
    return final_input
            
print(user_input_ckeck(look_for='songs', range_u=33))

