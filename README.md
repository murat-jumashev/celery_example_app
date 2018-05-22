# Example app with Celery registered as a Django app
## About:
When you visit the index page (e.g. locahost:8000) a celery task will send a dummy email to site admin.
Yep, this is a dummy celery task showcase :)

## OS dependencies:
1. Install redis-server:
```bash
sudo add-apt-repository ppa:chris-lea/redis-server
sudo apt-get update
sudo apt-get install redis-server
```
2. Check if it is running:
```bash
redis-cli ping
```
You should get PONG as a response
3. Done.

## Python dependencies (Python3):
1. Create a virtualenv:
```bash
python3 -m venv env
```
2. Activate the virtualenv:
```bash
source env/bin/activate
```
3. Install project dependencies:
```bash
pip install -r requirements.txt
```

## How to run:
1. Run migrations:
```bash
./manage.py migrate
```
2. Run dev server:
```bash
./manage.py runserver
```
3. In another terminal run:
```bash
celery -A apps.taskapp.celery -l worker info
```
