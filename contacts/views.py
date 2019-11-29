from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from contacts.models import Contacts


def index(request):
    return render(request,'contacts/contacts.html',)

def leave_feedback(request):
    # try:
    #      a=Contacts.objects.get(id=contact_id)
    # except:
    #     raise Http404("Статься не найдена")
    # if request.method=='POST':
    a = Contacts.objects.create(Firstname=request.POST['firstname'],Lastname=request.POST['lastname'],Email=request.POST['email'],Phone=request.POST['contacts'],Comment=request.POST['text'])

    return render(request,'contacts/contacts.html')