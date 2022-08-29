import user
from pprint import pprint
import yadisk
from vk_api import get_photo_dict
from datetime import datetime

ya = yadisk.YandexDisk(token=user._ya_token)
dict = get_photo_dict(user._vk_self_id)

counter = 0
success = 0

# pprint(dict)

for item in dict['response']['items']:
    counter = len(item['sizes'])
    for size in item['sizes']:
        if size['type'] == 'w':
            good_look_date = datetime.fromtimestamp(item["date"]).strftime("%Y, %d %B")
            ya.upload_url_to_disk(f'test/{good_look_date}- {item["likes"]["count"]} likes.jpg', size['url'])
            success += 1
            print(f'Записано {success} из {counter}')








