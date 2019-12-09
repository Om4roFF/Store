from django.urls import path
from django.conf.urls import url,include

from . import views
from django.conf.urls.static import static
from django.views.generic import ListView,DetailView
from django.db import models
from .models import Article,Comment


app_name='newsApp'
urlpatterns = [
    # url(r'^$',ListView.as_view(queryset=Article.objects.all(),template_name="../templates/newsApp/posts.html"))
    url('^$', views.index,name='latest_articles_list'),
    path('<int:article_id>/',views.detail,name='detail'),
    path('<int:article_id>/leave_comment',views.leave_comment,name='leave_comment'),
]