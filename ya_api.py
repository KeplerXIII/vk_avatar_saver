from pprint import pprint
import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_url_to_disk(self, ya_disk_file_path, file_path_url):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {
            "path": ya_disk_file_path,
            "url": file_path_url
        }
        response = requests.post(upload_url, headers=headers, params=params)
        response.raise_for_status()


    def create_folder(self, folder):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {
            "path": folder,
        }
        response = requests.put(url, headers=headers, params=params)
        status_code = response.status_code
        if status_code == 201:
            print(f'Папка {folder} создана')
        elif status_code == 409:
            print(f'Папка {folder} уже существует')
        else:
            response.raise_for_status()