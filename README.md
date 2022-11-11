## Task

1. Install `redis-server` on your machine
2. Install `celery` as a project dependency
3. Install `redis` as a project dependency
4. Integrate celery with the project
   - Allow for defining celery config options in `settings.py` module
   - Celery config options should have the prefix `CELERY_CONF`
     - for example: `CELERY_CONF_TIMEZONE`, `CELERY_CONF_RESULT_BACKEND`
5. Setup a gmail email to use for this project to send emails from
6. Use `django-environ` to import your secure environment variables like the redis server address or email credentials
7. Define a task in `albums/tasks.py` or whatever `related_name` you provided for celery's `autodiscover_tasks()` method
8. Define a task that receives the artist and album data you need as arguments and send the artist a congratulation email.
   - remember: the data the task receives must be serializable
9. Use a post-save signal or override `Album.save()` and each time an album is created **asynchronously call** the task that you defined in the previous step
10. Define another task that achieves `Use case 2.` and use celery's default beat scheduler `PersistentScheduler` to run the task every 24 hours
    - Define the `beat_schedule` in `settings.py` like so:
    ```
    CELERY_CONF_BEAT_SCHEDULE = {
        'add-every-30-seconds': {
            'task': 'tasks.add',
            'schedule': 30.0,
            'args': (16, 16)
        },
    }
    ```
    - Read: There is another way to define periodic tasks during runtime by storing the beat schedule in django's database and using django admin to define each task's schedule. See [`django-celery-beat`](https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes)
