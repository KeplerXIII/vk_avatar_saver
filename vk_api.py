import user
import requests

def get_photo_dict(vk_id):
    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': vk_id,
        'access_token': user._vk_token,
        'album_id': "profile",
        'photo_sizes': '1',
        'extended': '1',
        'v': '5.131'
    }
    res = requests.get(URL, params=params)
    res = res.json()

    return res
