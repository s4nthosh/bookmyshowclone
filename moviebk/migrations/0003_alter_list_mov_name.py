# Generated by Django 4.1.6 on 2023-02-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0002_remove_movies_banner_movies_banner_1_movies_banner_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_mov',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
