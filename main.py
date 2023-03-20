from modules import yauploader as yap
from modules import vkparser as vkp


def run_yauploader(token):
    """Принимает токен и ссылку на загрузку. 
    Возвращает сообщение о ходе выполнения загрузки
    """
    token = input('Token pls from YaDisk: ')
    path_to_file = 'image.jpeg'
    uploader = yap.YaUploader(token)
    print(uploader.upload('image.jpeg', path_to_file))

