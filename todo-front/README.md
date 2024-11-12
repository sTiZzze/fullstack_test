1. Билд докера
```
docker build -t react-application .
```
2. Запускаем
```
docker run -d -p 3000:3000 react-application
```
## Urls

Создание юзера: http://localhost:3000/signup

Логин юзера: http://localhost:3000/login

Задачаи: http://localhost:3000/tasks