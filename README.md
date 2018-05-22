# Example app with Celery registered as a Django app
## About:
When you visit the index page (e.g. locahost:8000) a celery task will send a dummy email to site admin.
Yep, this is a dummy celery task showcase :)
To see how the things were implemented, open:
1. apps/taskapp/celery.py -- this is where celery app was created and configured
2. config/settings.py -- see INSTALLED_APPS to see how celery was registered
3. apps/website/tasks.py -- a task called send_email_async is registed here. It sends an email with 10 seconds delay
4. apps/website/views.py -- a place where IndexView calls send_email_to_admin() which calls send_email_async() task

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
