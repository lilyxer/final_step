import requests
from datetime import datetime

class VkParser:
    """Производит поиск по альбомам пользователя, если настройки
    приватности позволяют.
    Собирает альбомы и фото в максимальном разрешении
    Возвращает словарь словарей 
    альбом: {фото: ссылка}"""
    def __init__(self, token: str, id: int, album_all: int):
        self._token = token
        self._id = id
        self._album_all = album_all
        self._url = 'https://api.vk.com/method/'
        
    def _search_albums(self) -> dict:
        """Вернет словарь известных нам альбомов
        ключи - id, значения - названия альбомов"""
        _album_dct = {'profile': 'Фотографии с моей страницы', 
                      'wall': 'Фотографии на моей стене'}
        if self._album_all:
            resp_alb = self._get_albums()
            if resp_alb:
                print(resp_alb)
                for album in resp_alb['response']['items']:
                    _album_dct.update({album['id']: album['title']})
        return _album_dct
    
    def _get_albums(self) -> dict|None:
        """Проверяем есть ли открытые альбомы у пользователя"""
        print('Смотрим альбомы пользователя\n')
        method = 'photos.getAlbums'
        params = {'access_token': self._token,
                  'v': 5.131,
                  'owner_id': self._id}
        resp = self._get_request(method=method, params=params)
        if resp.get('error'):
            print(f'Альбомы у {self._id} получен ответ')
            print('Сработали настройки приватности')
            print(resp['error']['error_msg'], end='\n\n')
            return
        return resp
    
    def _get_request(self, method: str, params: dict) -> dict|None:
        """Возвращает словарь с ответом от сервера"""
        resp = requests.get(url=f'{self._url}{method}', params=params)
        if resp.status_code == 200:
            return resp.json()
        print('Сработали настройки приватности\n')
    
    def get_our_albums(self) -> dict:
        """Получаем словари по известным группам
        Полученные словари передаем на парсинг"""
        _album_dct = self._search_albums()
        squeeze = {}
        method = 'photos.get'
        params = {'access_token': self._token,
                  'v': 5.131,
                  'owner_id': self._id,
                  'album_id': None,
                  'extended': 1}
        for id, album in _album_dct.items():
            params['album_id'] = id
            response = self._get_request(method=method, params=params)
            if response:
                print(f'Альбом {album} получен ответ')
                squeeze.update(self._parsing_to_file(album, response))
        return squeeze
            
    def _parsing_to_file(self, name: str|int, response: dict) -> dict:
        """Получаем словари, вытаскиваем из него ссылку на макc разрешение
        дату загрузки и количество лайков.
        Возвращаем словарь для дальнейшей выгрузки в файл"""
        squeeze = {}
        for photo in response['response']['items']:
            date = datetime.strftime(datetime.fromtimestamp(photo['date']), 
                                     '%Y-%m-%d %H_%M')
            url = photo['sizes'][-1]['url']
            likes = photo['likes']['count']
            squeeze[f'{likes}_{date}'] = url
        print(f'Альбом {name} получено {len(squeeze)} '
              'фото в максимальном размере\n')
        return {f'{name}': squeeze}
            
    def __str__(self):
        return (f'привет я - {self.__class__.__name__}\n'
                f'помогу тебе получить все ссылки на фотографии из альбома'
                f' пользователя {self._id}')