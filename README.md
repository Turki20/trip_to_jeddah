# trip_to_jeddah
"Trip to Jeddah" is a Django-based web application that aims to provide a platform for organizing trips to Jeddah according to the user's preferences. The application allows users to explore Jeddah's attractions, restaurants, and activities, save and share their itinerary in a PDF file, and modify it as desired. The application also allows users to view all the places, restaurants, and events in Jeddah, add comments and ratings, and interact with users.

## Features
- Displays tourist attractions in Jeddah.
- Provides information on the best restaurants in the city.
- A system for arranging trips based on user preferences.
- Easy-to-use interface.
- Displays locations, restaurants, ratings, and reviews.

## Requirements
Before installing the project, ensure that you have the following prerequisites installed:
- Python 3.13.2
- MySQL
- pip

## Installation and Setup
* terminal (windows)
```bash
git clone https://github.com/Turki20/trip_to_jeddah.git
cd trip_to_jeddah
```
```bash
python -m virtualenv env
```
```bash
cd env/Scripts
activate
cd ..
cd ..
```
```bash
pip install -r requirements.txt
```

* MySQL
```sql
CREATE DATABASE trip_to_jeddah;
```
* setting.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trip_to_jeddah',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
* terminal (windows)
``` bash
python manage.py makemigrations
python manage.py migrate
```
```bash
python manage.py runserver
```

