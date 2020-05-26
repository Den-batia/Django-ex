from NewJ.celery import app
import time

@app.task
def asd(a):
    time.sleep(10)
    return a

