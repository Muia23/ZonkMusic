# Generated by Django 3.2.4 on 2021-06-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonkmusicke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeShows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showdate', models.CharField(max_length=60)),
                ('showtitle', models.CharField(max_length=120)),
                ('showhost', models.CharField(max_length=60)),
                ('eattime', models.CharField(max_length=60)),
                ('cattime', models.CharField(max_length=60)),
            ],
        ),
    ]
