from django_playground import app
import time


# Define a Celery task using the task decorator.
@app.task
def add(x, y):
    time.sleep(5)
    return x + y
