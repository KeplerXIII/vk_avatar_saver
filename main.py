import user
from pprint import pprint
import yadisk
from vk_api import get_photo_dict
from datetime import datetime

ya = yadisk.YandexDisk(token=user._ya_token)
dict = get_photo_dict(user._vk_self_id)

def synchronization_vk_ya():
    success = 0
    for item in dict['response']['items']:
        counter = len(dict['response']['items'])
        for size in item['sizes']:
            if size['type'] == 'w':
                good_look_date = datetime.fromtimestamp(item["date"]).strftime("%Y, %d %B")
                ya.upload_url_to_disk(f'test/{good_look_date}- {item["likes"]["count"]} likes.jpg', size['url'])
                success += 1
                print(f'Записано {success} из {counter}')


pprint(dict)








