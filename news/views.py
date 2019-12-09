from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from .models import Article,Comment
from django.urls import reverse
import requests
from bs4 import BeautifulSoup as BS
def index(request):
    latest_articles_list=Article.objects.order_by('-pub_date')[:7]
    return render(request,'news/posts.html',{'latest_articles_list':latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comment_list=a.comment_set.order_by('-id')[:20]
    return render(request,'news/details.html', {'article': a,'latest_comment_list': latest_comment_list})


def leave_comment(request, article_id):
    try:
        a=Article.objects.get(id=article_id)
    except:
        raise Http404("Статься не найдена")

    a.comment_set.create(author_name=request.POST['name'],comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('newsApp:detail',args=(a.id,)))

