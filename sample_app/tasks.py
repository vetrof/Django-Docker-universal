from celery import shared_task
from django.core.cache import cache
import random

@shared_task()
def printer():
    print("***** hello!!! *****")
    x = random.randint(1, 9999999)
    cache.set(f'random_{x}', x)
    return 'Done'
