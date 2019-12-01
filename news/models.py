from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.timezone import now


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_content = RichTextUploadingField()
    article_img = models.ImageField(null=True,blank=True)
    pub_date = models.DateTimeField(null=True,default=now)
    article_short_content = models.TextField(max_length=300)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name='Статья'
        verbose_name_plural ='Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    author_name=models.CharField('имя автора',max_length=50)
    comment_text=models.CharField('текст комментария',max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
