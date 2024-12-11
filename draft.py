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


def user_input_ckeck():
    # user_input = ''.join(user_input.split())
    #check for numeric input only
    user_input = input('Please type numbers of the songs you want to remove: ')
    if ''.join(user_input.split()).isnumeric():
        print('Input is numeric')
        return [int(i) for i in user_input.split()]
    else:
        print('Make sure you type only numbers separated with space')
        return user_input_ckeck()

#['collaborative', 'description', 'external_urls', 'href', 'id', 'images', 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'])



uinput = [int(i) for i in input().split()]
t_f = [i in range(10) for i in uinput]
print(all(t_f))
