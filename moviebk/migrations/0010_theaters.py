# Generated by Django 4.1.6 on 2023-02-20 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0009_rename_movies_list_mov_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='theaters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_name', models.CharField(max_length=200)),
                ('time1', models.CharField(blank=True, max_length=20, null=True)),
                ('time2', models.CharField(blank=True, max_length=20, null=True)),
                ('time3', models.CharField(blank=True, max_length=20, null=True)),
                ('time4', models.CharField(blank=True, max_length=20, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviebk.main')),
            ],
        ),
    ]
