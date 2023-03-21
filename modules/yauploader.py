import requests

class YaUploader:
    """Создает папку на Я.Диске, если уже существует сверится со списком
    фйлов. Загрузит фото для бэкапа"""
    
    def __init__(self, token: str) -> None:
        self._token = token
        self._headers = {
                        'Accept': 'application/json',
                        'Authorization': self._token}
        self._url = 'https://cloud-api.yandex.net/v1/disk/'

    def upload_photos(self, file_dict: dict, folder_name: str) -> str:
        """Получает на вход словарь с файлами и ссылками, создаст папку
        либо сверится по дубликатам в этой папке, загрузит фото"""
        folder_name = self._create_folder_path(folder_name)
        folder, files = folder_name
        file_dict = {key: value for key, value in file_dict.items() 
                     if key not in files}
        for name, link in file_dict.items():
            params = {'path': f'{folder}/{name}',
                      'url': link,
                      'overwrite': 'false'}
            resp = requests.post(f'{self._url}resources/upload', 
                          headers=self._headers, params=params)
        return resp.json()
        
    def _get_link(self, folder_name: str) -> dict:
        """Вернет имена файлов если папка была создана ранее"""
        params = {'path': folder_name}
        resource = requests.get(f'{self._url}resources', 
                                headers=self._headers, 
                                params=params)
        if resource.status_code == 200:
            resource = resource.json()['_embedded']['items']
            return [elem['name'] for elem in resource]
        print(f'Сервер вернул код {resource.status_code}')
        raise RuntimeError 

    def _create_folder_path(self, folder_name: str) -> str|None:
        """Создание папки на диске
        Если папку создать не получилось вернет сообщение
        Возбудит исключение"""
        params = {'path': folder_name}
        response = requests.put(f'{self._url}resources', 
                                headers=self._headers, 
                                params=params)
        if response.status_code == 201:
            return folder_name, []
        elif response.status_code == 409:
            return folder_name, self._get_link(folder_name)
        print(f'Сервер вернул код {response.status_code}')
        raise RuntimeError

    def __str__(self) -> str:
        return 'Я создан чтобы делать резервные копии на Я.Диск'


if __name__ == '__main__':
    path_to_file = 'image.jpeg'
    token = input('Token pls ')
    uploader = YaUploader(token)
    print(uploader.upload_image('image.jpeg', path_to_file))
