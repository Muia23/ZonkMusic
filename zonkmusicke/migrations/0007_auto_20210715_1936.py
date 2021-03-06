# Generated by Django 3.2.4 on 2021-07-15 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zonkmusicke', '0006_auto_20210715_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeblogs',
            name='blogurl1',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeblogs',
            name='blogurl2',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeblogs',
            name='blogurl3',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
