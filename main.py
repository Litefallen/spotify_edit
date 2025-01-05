import requests
import httpx
import dotenv
import os
import asyncio
import base64
import fastapi
import webbrowser
from fastapi import Query
from getting_library_data import get_tracks_data
from library_modification import remove_songs
from download_music import get_your_music, folder_mk
from fastapi.responses import RedirectResponse
from song_search import load_json_library, user_input_ckeck
import uvicorn
# Hide sensitive data   
dotenv.load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

api = fastapi.FastAPI()
@api.get('/end')
def end_page():
    return 'You may close this tab now'


@api.get('/callback/')
async def get_token(code=Query):
    auth_code = code
    base64_auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {'Authorization': f'Basic {base64_auth}', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'authorization_code', 'code': auth_code, # GET TOKEN FOR ITEMS CHANGE
            'redirect_uri': 'http://127.0.0.2:8000/callback/'}
    req = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    at = req.json()
    headers = {'Authorization': f'Bearer {at['access_token']}'}
    user_info = requests.get('https://api.spotify.com/v1/me', headers=headers)
    user_info = user_info.json()
    while True:
        # user_input = user_input_ckeck(look_for='playlist',range_u=2)
        user_input = user_input_ckeck(look_for='fav_or_pl',range_u=2)
        print(user_input)
        user_data = get_tracks_data(headers, username=user_info['display_name'],user_input=user_input)
        songs_to_remove = load_json_library(user_data[0])
        
        print(songs_to_remove)
        remove_songs(tracks_id=songs_to_remove,playlist=user_data[2], headers=headers)
        print('The songs has been removed from the playlist')

    

    
    # async with httpx.AsyncClient() as client:
    #     print('Getting fav songs list...')
    #     await asyncio.gather(
    #         *[get_fav_songs(at, client, 0 + 50 * c) for c in range(total_amount // num_cur_tracks + 1)])
    # for i in music_list:
    #     await get_your_music(i[0], i[1])  
    # print('All songs were downloaded')
    return RedirectResponse('/end')

scopes = 'playlist-read-private user-read-private user-library-read user-library-modify playlist-modify-private playlist-modify-public'
if __name__ == "__main__":
    # Open a web browser to initiate the Spotify authorization process
    webbrowser.open(
        f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&redirect_uri=http://127.0.0.2:8000/callback/&scope={scopes}&show_dialog=True')
    uvicorn.run("main:api", host="127.0.0.2", port=8000, log_level=None)


