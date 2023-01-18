<h1> Решение тестового задания</h1>

# Как установить проект 
### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Dreamseller4u/Plates_FASTAPI.git
```
### Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

### Подготовка базы данных Postgresql для Linux:
```
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres createdb plates_db
sudo -u postgres psql
\connect plates_db
Output: You are connected to database "plates_db" as user "posgres" via socket in "/var/run/postgresql" at port "5432".
\d 
Output"
                  List of relations
 Schema |          Name           |   Type   | Owner
--------+-------------------------+----------+-------
 public | plates              | table    | sammy
 public | plates_equip_id_seq | sequence | sammy
(2 rows) 
```
### Запустить проект:
```
cd src/
uvicorn main:app --reload
http://127.0.0.1:8000/docs
```

### PS:
```
Для использования Users из бд раскомментировать закомментированый код в файлай src/

```

### Стек технологий: Python 3, FASTAPI, PostgreSQL
### Автор проекта - Кочевых Никита