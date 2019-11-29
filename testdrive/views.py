from django.shortcuts import render

def index(request):
    return render(request,'testdrive/test-drive.html')
