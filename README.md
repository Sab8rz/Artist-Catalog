# Инструкция по запуску

### Склонируйте репозиторий:
git clone https://github.com/Sab8rz/Artist-Catalog.git

### Создайте и активируйте виртуальное окружение:
python -m venv venv

.\venv\Scripts\activate

### Установите зависимости
pip install -r requirements.txt

### Перейдите в каталог artistcatalog:
cd artistcatalog

### Выполните миграции и создайте суперпользователя:
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

### Запустите сервер
python manage.py runserver

#### Доступные адреса:
http://127.0.0.1:8000/swagger/

http://127.0.0.1:8000/redoc/

http://127.0.0.1:8000/admin/ - админ-панель для управления данными

http://127.0.0.1:8000/api/artists/ - список всех исполнителей

http://127.0.0.1:8000/swagger/artists/айди-исполнителя/ - данные по исполнителю с указанным id

http://127.0.0.1:8000/api/albums/ - список всех альбомов

http://127.0.0.1:8000/swagger/artists/айди-альбома/ - данные по альбому с указанным id

http://127.0.0.1:8000/api/songs/ - список всех песен

http://127.0.0.1:8000/swagger/artists/айди-песни/ - данные по песне с указанным id
