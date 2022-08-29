import user
from pprint import pprint
import yadisk
from vk_api import get_photo_dict

ya_uploader = yadisk.YandexDisk(user._ya_token)
dict = get_photo_dict(user._vk_self_id)


for item in dict['response']['items']:
    for size in item['sizes']:
        if size['type'] == 'w':
            dict[item['date']] = size['url']




