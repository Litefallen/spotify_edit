

# get tracks from fav
def get_tracks_data(headers, username, user_input):
    import json
    import requests
    headers = headers
    # print("1. Modify one of your playlists")
    # print("2. Modify your 'Liked Songs'")



    # add errorckeck
    # u_input = int(input('Please, type 1 or 2')) 
    if user_input ==1:
        #getting all playlists
        user_playlists = requests.get('https://api.spotify.com/v1/me/playlists',headers=headers)
        user_playlists = user_playlists.json()
        user_playlists = user_playlists['items']
        users_playlists_info = dict()
        for i in range(len(user_playlists)):
            if isinstance(user_playlists[i], dict): # errorcheck for spotify editorial playlists
                if user_playlists[i]['owner']['display_name'] == username: # check if we get personal users playlists only
                    users_playlists_info[user_playlists[i]['name']] = user_playlists[i]['tracks']
        #user to choose which playlist to modify
        for i in enumerate(list(users_playlists_info), start = 1):
            print(f'{i[0]}. {i[1]}')
        u_input = int(input('please choose the playlist you want to modify: ')) - 1
        u_input = list(users_playlists_info)[u_input]
        rqst_url = f'{users_playlists_info[user_input]['href']}'
    if user_input ==2:
        user_input = 'Liked Songs'
        rqst_url = 'https://api.spotify.com/v1/me/tracks'
    tracks_artist_dict = {}
    tracks_dict = {}
    offset_coef = 0
    params={'limit': '50', 'offset': 0}

    print('Fetching data...')
    while True:
        params['offset'] = 0 + 50 *offset_coef
        req_data = requests.get(rqst_url, headers=headers, params=params)
        req_data = req_data.json()
        for i in req_data['items']:
            track_dict = i['track']
            track_id = track_dict['id']
            tracks_artist = track_dict['artists'][0]['name']
            tracks_title = track_dict['name']
            tracks_artist_dict.setdefault(tracks_artist, {tracks_title:track_id})
            tracks_artist_dict[tracks_artist].update({tracks_title:track_id})
            tracks_dict[tracks_title] = track_id
        if params['offset'] > req_data['total']:
            break
        offset_coef +=1
    print('Finished.')
    return (tracks_artist_dict, tracks_dict, rqst_url)