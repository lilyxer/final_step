from modules import yauploader as yap
from modules import vkparser as vkp
import json

def run_yauploader(token: str, my_d: dict) -> str:
    """Принимает токен и ссылку на загрузку. 
    Возвращает сообщение о ходе выполнения загрузки
    """
    uploader = yap.YaUploader(token)
    for album, photo in my_d.items():
        print(uploader.upload_photos(file_dict=photo, 
                                 folder_name=album, count=5))

def run_vkparser(token: str) -> dict:
    """Принимает токен и ссылку на id профиля """
    owner_id = input('Введите id пользователя')
    if owner_id.isdigit():
        owner_id = int(owner_id)
    else:
        print('Мы ждем цифровой идентефикатор. \n'\
              'Программу необходимо перезапустить')
        return
    print('Ищем все фотоальбомы или только профиля?')
    answer = int(input('1 - все, 0 - только профиля: '))
    if answer:
        print('Вы выбрали все фотографии пользователя')
    else:
        print('Вы выбрали только фотографии профиля')
    
    parser = vkp.VkParser(token=token, id=owner_id, album_all=answer)
    return parser.get_our_albums()


if __name__ == '__main__':
    my_choice = run_vkparser(input('Token pls for VK: '))
    if my_choice:
        all_photo = sum(len(v) for k, v in my_choice.items())
        with open('my_photo_from_vk.json', 'w', encoding='utf-8') as file:
            json.dump(my_choice, file, indent=4, ensure_ascii=False)
        print(f'В файл выгружено {all_photo}\n'
              f'Запускаем загрузчик')
        run_yauploader(input('id pls from YaDisk: '), my_choice)
        
        