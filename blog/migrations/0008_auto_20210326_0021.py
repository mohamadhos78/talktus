# Generated by Django 3.1.7 on 2021-03-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Urlimage',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Urlimage',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Urlvideo',
            field=models.URLField(blank=True),
        ),
    ]
