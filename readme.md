## Как запускать

### Создать виртуальную среду (не обязательно)

```sh
python3 -m venv env
```

```sh
source ./env/bin/activate
```

### Установить зависимости

```sh
python3 -m pip install -r requirements.txt
```

### Можно запускать 

```sh
python3 uploader.py
```

### в пакете aiohttp встроен FTP сервер по умолчанию ( можно использовать для проверки )

```sh
python3 -m aioftp
```
