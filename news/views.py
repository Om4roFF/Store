from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from .models import Article,Comment
from django.urls import reverse
import requests
from bs4 import BeautifulSoup as BS
def index(request):
    latest_articles_list=Article.objects.order_by('-pub_date')[:7]
    return render(request,'news/posts.html',{'latest_articles_list':latest_articles_list})


def detail(request,article_id):
    try:
        a=Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comment_list=a.comment_set.order_by('-id')[:20]
    return render(request,'news/details.html',{'article':a,'latest_comment_list':latest_comment_list})

def leave_comment(request,article_id):
    try:
        a=Article.objects.get(id=article_id)
    except:
        raise Http404("Статься не найдена")

    a.comment_set.create(author_name=request.POST['name'],comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('newsApp:detail',args=(a.id,)))

def parser(request):
    r = requests.get(r'https://kolesa.kz/content/news/')
    html = BS(r.content, 'html.parser')
    l = []
    for i in html.select('#main-list'):
        head = i.select('a')
        for j in head:
            link = 'https://kolesa.kz/content/news' + j.get('href')
            l.append(link)
    try:
        for i in range(7):
            s = requests.get(l[i])
            soap = BS(s.content, 'html.parser')
            for x in soap.select('.wrapper'):
                title = x.select('.article-title')
                content = x.select('.entry-content')
                summary = x.select('.content-summary')
                img = x.select('img')
                date = x.select('.entry-date')
                if (len(title)):
                    Article.objects.create(article_title=title[0], article_short_content=summary[0],
                                               article_content=content[0])
                    print(title[0].text)
                    print(content[0])
                    print(summary[0])
                    print(img[0])
                    print(date[0])
            print()
    except:
        raise Http404("Статья не найдена")
    return render(requests,'news/posts.html')

