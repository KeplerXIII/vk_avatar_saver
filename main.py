from datetime import datetime
from tqdm import tqdm
import user
import ya_api
import operator
import vk_api
import json


def vk_yadisk_parser(VK_TOKEN, YA_TOKEN, VK_ID, folder):
    success = 0
    result = []
    vk = vk_api.Vkontakte(token=VK_TOKEN)
    ya = ya_api.YandexDisk(token=YA_TOKEN)
    vk_response = vk.get_photo_dict(VK_ID)
    if 'error' in vk_response:
        print(f'ID {VK_ID} отключен. Введите валидный ID.')
        return
    counter = len(vk_response['response']['items'])
    ya.create_folder(folder)
    print(f'Найдено {counter} фотографий')
    quantity = int(input("Введите количество загружаемых фото: "))
    if quantity == 0:
        print(f'Загрузка отменена')
        return
    pbar = tqdm(total=quantity, desc='Фото загружаются', colour='green')
    for item in vk_response['response']['items']:
        good_look_date = datetime.fromtimestamp(item["date"]).strftime("%Y, %d %B")
        item['sizes'].sort(key=operator.itemgetter('height'))
        ya.upload_url_to_disk(f'{folder}/{good_look_date} - {item["likes"]["count"]} likes.jpg',
                              item['sizes'][-1]['url'])
        result.append({'file_name': f'{good_look_date} - {item["likes"]["count"]} likes.jpg',
                       'size': f'{item["sizes"][-1]["type"]}'})
        success += 1
        pbar.update(1)
        if success >= quantity:
            break
    pbar.close()
    with open("data_file.json", "w") as f:
        json.dump(result, f)
        print(f'Загрузка завершена успешно. Создан отчёт о загрузке - data_file.json')


if __name__ == "__main__":

    VK_TOKEN = user._vk_token  # Для работы необходимо указать ваш токен
    YA_TOKEN = user._ya_token  # Для работы необходимо указать ваш токен
    folder = input('Введите название папки для сохранения: ')
    VK_ID = input('Введите ID пользователя ВКонтакте: ')

    vk_yadisk_parser(VK_TOKEN, YA_TOKEN, VK_ID, folder=folder)


