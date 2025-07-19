# LSM-system_drf - Django REST Framework проект

## Описание проекта
Проект представляет собой веб-приложение на Django REST Framework с использованием:
- PostgreSQL
- Redis
- Celery
- Celery Beat

## Требования
- Docker (версия 20.10.0+)
- Docker Compose (версия 1.29.0+)
- `.env` файл с необходимыми переменными окружения

## Запуск проекта

### 1. Подготовка окружения
Создайте файл `.env` в корне проекта с содержимым:

```env
# Настройки PostgreSQL
NAME=your_db_name
USER=your_db_user
PASSWORD=your_db_password

# Настройки Redis
REDIS_URL=redis://redis:6379/0

# Настройки Django
SECRET_KEY=your_secret_key
DEBUG=True

# Настройки Celery
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0