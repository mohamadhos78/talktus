# Generated by Django 3.1.7 on 2021-03-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210306_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='hello world is my slogan', max_length=512),
            preserve_default=False,
        ),
    ]