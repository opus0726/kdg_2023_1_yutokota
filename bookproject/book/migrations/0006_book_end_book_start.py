# Generated by Django 4.2.6 on 2024-01-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='start',
            field=models.DateField(null=True),
        ),
    ]
