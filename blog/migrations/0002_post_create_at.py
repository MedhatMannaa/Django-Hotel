# Generated by Django 3.1.1 on 2020-09-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]