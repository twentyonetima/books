# Generated by Django 4.1.2 on 2022-10-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='author', max_length=255, verbose_name='Author'),
            preserve_default=False,
        ),
    ]
