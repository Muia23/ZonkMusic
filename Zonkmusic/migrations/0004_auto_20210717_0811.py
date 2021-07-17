# Generated by Django 3.1.3 on 2021-07-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zonkmusic', '0003_auto_20210717_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='About1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abouttitle', models.CharField(max_length=60)),
                ('abouttexta', models.TextField()),
                ('abouttextb', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='About2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abouttitle', models.CharField(max_length=60)),
                ('abouttexta', models.TextField()),
                ('abouttextb', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='About3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abouttitle', models.CharField(max_length=60)),
                ('abouttexta', models.TextField()),
                ('abouttextb', models.TextField()),
                ('abouttextc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
