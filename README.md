# Example app with Celery registered as a Django app

## How to run:
1. Run server:
```bash
./manage.py runserver
```
2. In another terminal run:
```bash
celery -A apps.taskapp.celery -l worker info
```
3. In yet another terminal run:
```bash
redis-server
```