# Generated by Django 4.1.6 on 2023-02-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0004_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
