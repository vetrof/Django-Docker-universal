from celery import shared_task


@shared_task()
def printer():
    print("***** hello!!! *****")
    return 'Done'
