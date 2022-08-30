from datetime import datetime
from pprint import pprint
import user
import yadisk
import operator
import vk_api

VK_TOKEN = user._vk_token
YA_TOKEN = user._ya_token
VK_ID = user._vk_self_id

def vk_yadisk_parser(VK_TOKEN, YA_TOKEN, VK_ID, quantity=5):
    success = 0
    result = []
    vk = vk_api.Vkontakte(token=VK_TOKEN)
    ya = yadisk.YandexDisk(token=YA_TOKEN)
    dict = vk.get_photo_dict(VK_ID)
    counter = len(dict['response']['items'])
    print(f'Найдено {counter} фотографий')
    for item in dict['response']['items']:
        good_look_date = datetime.fromtimestamp(item["date"]).strftime("%Y, %d %B")
        item['sizes'].sort(key=operator.itemgetter('height'))
        ya.upload_url_to_disk(f'test/{good_look_date} - {item["likes"]["count"]} likes.jpg', item['sizes'][-1]['url'])
        result.append({'file_name': f'{good_look_date} - {item["likes"]["count"]} likes.jpg', 'size': f'{item["sizes"][-1]["type"]}'})
        success += 1
        print(f'Сохранено {success} из {counter}')
        if success >= quantity:
            break

    pprint(result)

vk_yadisk_parser(VK_TOKEN, YA_TOKEN, VK_ID)









