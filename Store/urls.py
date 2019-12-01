from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('contacts/',include('contacts.urls')),
    path('news/',include('news.urls')),
    path('testdrive/',include('testdrive.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
