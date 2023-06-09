<div><p>Возможна такая ситуация, что мы хотим показать друзьям фотографии из социальных сетей, но соц. сети могут быть недоступны по каким-либо причинам. Давайте защитимся от такого.<br>
Нужно написать программу для резервного копирования фотографий с профиля(аватарок) пользователя vk в облачное хранилище Яндекс.Диск.<br>
Для названий фотографий использовать количество лайков, если количество лайков одинаково, то добавить дату загрузки.<br>
Информацию по сохраненным фотографиям сохранить в json-файл.</p>
<h3><strong>Задание:</strong></h3>
<ul>
<li>Нужно написать программу, которая будет:</li>
<li>Получать фотографии с профиля. Для этого нужно использовать метод <a href="https://dev.vk.com/method/photos.get" target="_blank">photos.get</a>.</li>
<li>Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.</li>
<li>Для имени фотографий использовать количество лайков.</li>
<li>Сохранять информацию по фотографиям в json-файл с результатами.</li>
</ul>
<p>*Обратите внимание: *токен для ВК можно получить выполнив <a href="https://docs.google.com/document/d/1_xt16CMeaEir-tWLbUFyleZl6woEdJt-7eyva1coT3w/edit" target="_blank">инструкцию</a>.</p>
<h3><strong>Входные данные:</strong></h3>
<p>Пользователь вводит:</p>
<ul>
<li>id пользователя vk;</li>
<li>токен с <a href="https://yandex.ru/dev/disk/poligon/" target="_blank">Полигона Яндекс.Диска</a>. <em>Важно:</em> Токен публиковать в github не нужно!</li>
</ul>
<h3><strong>Выходные данные:</strong></h3>
<ol>
<li>json-файл с информацией по файлу:</li>
</ol>
<code>    [{
    <span class="hljs-attr">"file_name"</span>: <span class="hljs-string">"34.jpg"</span>,
    <span class="hljs-attr">"size"</span>: <span class="hljs-string">"z"</span>
    }]
</code>
<ol start="2">
<li>Измененный Я.диск, куда добавились фотографии.​​</li>
</ol>
<h3><strong>Обязательные требования к программе:</strong></h3>
<ol>
<li>Использовать REST API Я.Диска и ключ, полученный с полигона.</li>
<li>Для загруженных фотографий нужно создать свою папку.</li>
<li>Сохранять указанное количество фотографий(по умолчанию 5) наибольшего размера (ширина/высота в пикселях) на Я.Диске</li>
<li>Сделать прогресс-бар или логирование для отслеживания процесса программы.</li>
<li>Код программы должен удовлетворять PEP8.</li>
<li>У программы должен быть свой отдельный репозиторий.</li>
<li>Все зависимости должны быть указаны в файле requiremеnts.txt.​</li>
</ol>
<h3><strong>Необязательные требования к программе:</strong></h3>
<ol>
<li>Сохранять фотографии и из других альбомов.</li>
<li>Сохранять фотографии на Google.Drive.</li>
</ol>
</div>