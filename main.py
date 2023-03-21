from modules import yauploader as yap
from modules import vkparser as vkp


def run_yauploader(token):
    """Принимает токен и ссылку на загрузку. 
    Возвращает сообщение о ходе выполнения загрузки
    """
    uploader = yap.YaUploader(token)
    print(uploader)
    print(help(uploader))
    # my_d = {'image.jpeg': 'https://habrastorage.org/getpro/habr/upload_files/977/76f/c8f/97776fc8f3274b55b16ef9ac4f37af32.png'}
    # print(uploader.upload_photos(file_dict=my_d, 
    #                              folder_name='Mikes_photo'))


if __name__ == '__main__':
    run_yauploader(input('Token pls from YaDisk: '))
