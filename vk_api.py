import requests

class Vkontakte:
    def __init__(self, token):
        self.token = token

    def get_photo_dict(self, vk_id):
        URL = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': vk_id,
            'access_token': self.token,
            'album_id': "profile",
            'photo_sizes': '1',
            'extended': '1',
            'v': '5.131'
        }
        res = requests.get(URL, params=params)
        res = res.json()

        return res

    def get_status(self, vk_id):
        url = ''