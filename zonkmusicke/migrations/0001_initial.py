# Generated by Django 3.2.4 on 2021-06-28 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutimg', models.FileField(upload_to='home')),
                ('abouttitle', models.CharField(max_length=60)),
                ('aboutpara1', models.TextField()),
                ('aboutpara2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeLanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landingbackground', models.FileField(upload_to='home')),
                ('landinglogo', models.FileField(upload_to='home')),
                ('landingheading', models.CharField(max_length=100)),
                ('landingtext', models.TextField()),
            ],
        ),
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
