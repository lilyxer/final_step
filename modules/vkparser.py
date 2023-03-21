import requests
import time
from datetime import datetime

class VkParser:
    def __init__(self, token, id):
        self._token = token
        self._id = id
        self._url = 'https://api.vk.com/method/'
        
    def _pars_name_and_bdate(self, res):
        """Смотрим есть ли дата рождения у юзера, если есть - 
        возвращаем кортеж из имени и даты"""
        time.sleep(0.1) # иначе банят
        reg_f = r'%d.%m.%Y'
        reg_l = r'%d.%m'
        for i in res.json()['response']:
            if 'bdate' in i:
                date = (datetime.strptime(i['bdate'], reg_f) if len(i['bdate']) > 
                        5 else datetime.strptime(i['bdate'], reg_l))
                return date.strftime('%d.%b'), i['first_name'], i['last_name']

    def _parametres(self):
        return  {'access_token': self._token,
                  'v': 5.131}
    
    def _get_request(self, method: str, params: dict) -> dict|None:
        """Возвращает словарь с ответом от сервера"""
        resp = requests.get(url=f'{self._url}{method}', params=params)
        if resp.status_code == 200:
            return resp
        raise ValueError
    
    def _get_group_members(self):
        """Получаем список членов группы"""
        method = 'groups.getMembers'
        params = {'group_id': self._id}
        params.update(self._parametres())
        return self._get_request(method=method, params=params)
    
    def _get_bdate_member(self, user):
        """Возвращает карточку участника группы"""
        method = 'users.get'
        params = {'user_ids': user,
                  'fields': 'bdate'}
        params.update(self._parametres())
        return self._get_request(method=method, params=params)
        
    def squeeze_request(self):
        data = self._get_group_members().json()
        print('получаем ответ от группы...')
        print('Бежим по айдишникам...')
        for users in data['response']['items']:
            response = self._get_bdate_member(users)
            r_user = self._pars_name_and_bdate(response)
            if r_user:
                print(*r_user)

            
if __name__ == '__main__':
    input_token =  input('Input token: ')
    input_id = 'presny_moscow' # input('Input name or id group: ')
    pars_vk = VkParser(token=input_token, id=input_id)
    pars_vk.squeeze_request()
