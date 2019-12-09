from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings

from testdrive.models import Testdrive


def index(request):
    return render(request,'testdrive/test-drive.html')


def add_testdrive(request):
    if request.method == 'POST':
        male = request.POST['male']
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        phone = request.POST['phone']
        email = request.POST['email']
        # mark = request.POST['mark']
        model = request.POST['model']
        Testdrive.objects.create(male=male, name=name, surname=surname, patronymic=patronymic,
                                 phone=phone, email=email, model=model)
        if email:
            subject = 'Тест-драйв'
            message = ' Спасибо за запись на тест-драйв,мы свяжемся с вами в ближайшее время. '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(subject, message, email_from, recipient_list)

    return render(request, 'testdrive/test-drive.html')

