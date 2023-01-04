# django-telegram-bot
Матеріал уроку №17 | Телеграм бот + панель адміністратора на Django

## Інформація по налаштуванню та запуску проекта

Всі команди для Linux

```bash
# Створення віртуального середовища python

python3 -m venv venv

# Активація віртуального середовища

source venv/bin/activate

# Встановлення бібліотек з файлу requirements

pip install -r requirements.txt

# Перехід в папку проекта

cd telegram/

# Міграції, запуск Django

python3 manage.py makemigrations
python3 manage.py migrate

# Створення суперкористувача

python3 manage.py createsuperuser

# Запуск Django

python3 manage.py runserver

```

## Токен бота

Токен бота треба прописати в файл telegram/bot/bot.py

```python
bot = telebot.TeleBot('Your-Bot-Token')
```
 
