# Generated by Django 4.1.6 on 2023-02-23 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0023_screen_theatre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='theatre',
        ),
        migrations.DeleteModel(
            name='booking',
        ),
        migrations.DeleteModel(
            name='screen',
        ),
    ]
