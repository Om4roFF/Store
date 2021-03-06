# Generated by Django 2.2.7 on 2019-12-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdrive', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testdrive',
            old_name='First_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='testdrive',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='testdrive',
            old_name='Last_name',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='testdrive',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='testdrive',
            name='Email',
        ),
        migrations.AddField(
            model_name='testdrive',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='testdrive',
            name='male',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='testdrive',
            name='mark',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='testdrive',
            name='model',
            field=models.CharField(default='Выберите модель', max_length=50),
        ),
        migrations.AddField(
            model_name='testdrive',
            name='patronymic',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
