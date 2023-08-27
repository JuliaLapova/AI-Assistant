[![License][license-shield]][license-url]
[![Github][github-shield]][github-url]



# Описание проекта



Умный корпоративный ассистент, который помогает быстро находить специализированную информацию по заранее определенным тематикам.

Пример взаимодействи с нашим АПИ можно посмотреть [здесь][demo-url-front].

## Основные возможности
АПИ чат-бота для корпоративного чата, который позволяет:
* Получать ответы на определенную тематику
* Добавлять источники информации
* Добавлять ответы на часто задаваемые вопросы
* Управлять доступом к боту и базой знаний

## Структура проекта


Проект состоит из 3-х частей:

<details>
  <summary><b><strong>АПИ</strong></b></summary>
  
  FastAPI приложение, которое предоставляет доступ к боту и базе знаний. 
    Приложение состоит из 3-х частей:

* АПИ чат-бота (простой и расширенный)
* АПИ базы знаний (добавление индексов)
* АПИ для администрирования проекта

</details>
<details>
  <summary><b><strong>База данных</strong></b></summary>
  
PostgreSQL база данных, которая хранит:
  * Информацию о компаниях
  * Информацию о ключах к АПИ
  * Информацию о запросах пользователей
  * Правила фильтрации запросов

</details>

<details>
  <summary><b><strong>База знаний</strong></b></summary>
  
  В базе знаний хранятся индексы:
  * Индекс для поиска ответов на вопросы, связанные с ТК
  * Индекс для поиска ответов на общие вопросы по бизнесу
  * Индекс для поиска ответов на вопросы, связанные с уплатой налогов
  * Индекс для поиска ответов на вопросы, связанные с бухучетом

</details>

Сборка проекта осуществляется с помощью `docker-compose`.

## Используемые технологии

В проекте используются следующие технологии:

* [![Python][python]][python-url]
* [![Fastapi][Fastapi]][Fastapi-url]
* [![Docker][Docker]][Docker-url]


## Веб-интерфейс пользователя

Пример интерфейса пользователя:


<details>
  <summary>Примечание</summary>
  
  В данный момент веб-интерфейс находится в разработке.
</details>


## Работа с API

<details>
  <summary>Интерфейс</summary>

  АПИ доступно по адресу `http://localhost:8000/docs`

  ![img][product-screenshot2]
</details>

<details>
  <summary>Документация</summary>

  Документация доступна по адресу `http://localhost:8000/redoc`
  
  ![img][product-screenshot3]
</details>

<details>
  <summary>Примеры запросов</summary>

1. HTTP запрос

    ```bash
    http://localhost:8000/api/chatbot_simple/1
    ```
   Параметры:
    * `user_input` - вопрос пользователя
    * `params` - параметры запроса
    * `api_key` - ключ для доступа к АПИ

    ```json
    {
      "user_input": "Что такое НДФЛ?",
      "question": {
        "api_key": "API_KEY"
      }
    }
   ```
2. CURL запрос

    ```bash
        curl -X 'POST' \
          'http://localhost:8000/api/chatbot_simple/1' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "user_input": "Что такое НДФЛ?",
          "question": {
            "api_key": "API_KEY"
          }
        }'
    ```

</details>

## Запуск проекта

Для запуска проекта необходимо:
1. Склонировать репозиторий
2. Перейти в папку проекта
3. Создать переменную окружения `OPENAI_API_KEY`
4. Создать папку для логов `sudo mkdir -m777 -p logs/fastapi`
5. Запустить проект с помощью команды `docker-compose up --build`
6. Перейти на `localhost:8000` для входа в веб-интерфейс

## Запуск АПИ без базы знаний и базы данных
```bash
docker run -d -p 8000:8000 -e OPENAI_API_KEY={your_key} --name smart_assistant smart_assistant
```

## Запуск без докера
1. Установить зависимости
```bash
pip install -r fastapi_app/requirements.txt
```
2. Запустить проект
```bash
cd fastapi_app
uvicorn fastapi_app.fastapp:app --reload --port 9000 --env-file config.env
```
где `config.env` - файл с переменными окружения:
```bash
OPENAI_API_KEY={your_key}
DEBUG=True
```

