from celery import shared_task
import time


@shared_task(name="send_mail")
def send_email_task(receiner, message, subject=None):
    time.sleep(5)
    print("end of send email")


@shared_task(name="jam_zadan")
def jam(a, b):
    return a+b
