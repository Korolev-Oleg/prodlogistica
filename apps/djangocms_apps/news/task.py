from celery_config import app


@app.task
def update_news():
    print(' done '.center(50))
