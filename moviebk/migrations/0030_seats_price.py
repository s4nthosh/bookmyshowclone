# Generated by Django 4.1.6 on 2023-02-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0029_alter_seats_seat_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
