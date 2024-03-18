# Generated by Django 4.2.6 on 2024-01-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_end_book_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('anime', 'アニメ'), ('game', 'ゲーム'), ('other', 'その他')], max_length=100),
        ),
    ]