import os

HOST = os.getenv("EXTERNAL_HOST") or "localhost:8000"
LOGO = "https://drive.google.com/uc?export=view&id=1g0KmrIILmwb0Vrxt-J-n0HFvQBDhk0Lr"

LOGO_HTML = f"""
<img src="{LOGO}" width="210" height="240">
"""

DESCRIPTION = f"""
{LOGO_HTML}

АПИ для работы с AI-ассистентом:

**Для пользователей**
* Получение ответа от AI-ассистента в обычном режиме

<details>
  <summary>**Для администраторов**</summary>
    <p>Для администраторов доступны все операции, описанные выше.</p>
    <p>Кроме того, администратор может:</p>
    <ul>
        <li>Добавлять новых пользователей</li>
    </ul>
</details>

"""

TAGS_METADATA = [
    {
        "name": "assistant",
        "description": "Documentation for AI assistant API is available here.",
        "externalDocs": {
            "description": "External docs",
            "url": f"http://{HOST}/redoc",
        },
    },
    # {
    #     "name": "files",
    #     "description": "Operations with files. For demo only. Not available in production.",
    # },
    # {
    #     "name": "tables",
    #     "description": "Database queries. For demo only. Not available in production.",
    # },
    # {
    #     "name": "users",
    #     "description": "Operations with users. For developers. These endpoints are not available in production."
    # },
    {
        "name": "healthcheck",
        "description": "Healthcheck endpoint. Returns 200 if the service is up and running.",
    },
]
