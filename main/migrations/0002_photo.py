# Generated by Django 2.2.7 on 2019-12-02 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.Car')),
            ],
        ),
    ]
