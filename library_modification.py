import requests
from song_search import load_json_library

def remove_songs(tracks_id:list, headers:dict, playlist): # remove songs with provided ID's
    if playlist == 'https://api.spotify.com/v1/me/tracks':
        json_for_request = {'ids':tracks_id}
    else:
        list_for_request = [{'uri':f'spotify:track:{song_id}'} for song_id in tracks_id]
        json_for_request = {'tracks':list_for_request,"snapshot_id": f"{playlist.split('/')[-2]}"}
    return requests.delete(f'{playlist}', headers=headers, json=json_for_request)
