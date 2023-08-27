# Описание проекта

Интеллектуальный консультант для сотрудников СПб ГКУ «МФЦ».

## Основные возможности
Умный консультант позволяет:
* Получать ответы на конкретный вопрос
* Получать ссылки на источники данных

## Структура проекта

Проект состоит из 3-х частей:

<details>
  <summary><b><strong>АПИ</strong></b></summary>
  FastAPI приложение, которое предоставляет доступ к боту и базе знаний. 
</details>


<details>
  <summary><b><strong>База знаний</strong></b></summary>
  
  В базе знаний хранятся индексы:
  * Индекс для поиска ответов на вопросы, связанные с услугами оказываемыми СПб ГКУ «МФЦ».

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
  <summary></summary>
 
[ССЫлка на веб интерфейс](http://31.129.97.70:8501/)

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

