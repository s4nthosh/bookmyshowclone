# Generated by Django 4.1.6 on 2023-02-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0030_seats_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='save_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=50)),
            ],
        ),
    ]
