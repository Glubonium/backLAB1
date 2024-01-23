## Для запуску у себе на ПК:

1. Клонувати файли репозиторія;
2. Налаштувати віртуальне середовища:
```
python3 -m venv venv
```
3. Активувати віртуальне середовище:
```
source ./venv/bin/activate
```
4. Посатвити всі залежності:
```
pip install -r requirements.txt
```
5. Збілдити образ за допомогою Dockerfile:
```
docker build --build-arg PORT=<your port> . -t <image_name>:latest
```
6. Запустити образ за допомогою Dockerfile:
```
docker run -it --rm --network=host -e PORT=<your port> <image_name>:latest
```
7. Збілдити образ за допомогою Docker_compose:
```
docker-compose build
```
8. Запустити образ за допомогою Docker_compose:
```
docker-compose up
```
