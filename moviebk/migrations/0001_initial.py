# Generated by Django 4.1.6 on 2023-02-14 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catrogies', models.CharField(max_length=50)),
                ('banner', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='list_mov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='')),
                ('Description', models.CharField(max_length=50)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviebk.movies')),
            ],
        ),
    ]
