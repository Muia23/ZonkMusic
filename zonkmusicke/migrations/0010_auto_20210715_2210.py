# Generated by Django 3.2.4 on 2021-07-15 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zonkmusicke', '0009_auto_20210715_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='staffimg',
            new_name='staffimg1',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staffname',
            new_name='staffname1',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='stafftitle',
            new_name='staffname2',
        ),
        migrations.AddField(
            model_name='staff',
            name='staffimg2',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffimg3',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffimg4',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffimg5',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffimg6',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffname3',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffname4',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffname5',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='staffname6',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='stafftitle1',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='stafftitle2',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='stafftitle3',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='stafftitle4',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='stafftitle5',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='stafftitle6',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
