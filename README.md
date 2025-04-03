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

## interface
<img src="https://github.com/user-attachments/assets/5b0cc2d4-cf74-440a-b1ea-488e3d61ff80" alt="App Interface" width="500"/>
<img src="https://github.com/user-attachments/assets/c72dab17-3e97-487b-b72d-dcde9a09887e" alt="App Interface" width="500"/>
<br>
<img src="https://github.com/user-attachments/assets/a03feac5-7542-4651-b100-83211daf2dcc" alt="App Interface" width="300"/>
<img src="https://github.com/user-attachments/assets/3dc730cd-c89b-4119-81eb-4c4e5443669d" alt="App Interface" width="300"/>
<img src="https://github.com/user-attachments/assets/33f1237b-ccf2-4e00-8c1e-1ad3f6f55bcc" alt="App Interface" width="300"/>


