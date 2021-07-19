# Generated by Django 3.1.3 on 2021-07-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abouttitle1', models.CharField(max_length=60)),
                ('abouttexta', models.TextField()),
                ('abouttextb', models.TextField()),
                ('abouttitle2', models.CharField(max_length=60)),
                ('abouttextc', models.TextField()),
                ('abouttextd', models.TextField()),
                ('abouttitle3', models.CharField(max_length=60)),
                ('abouttexte', models.TextField()),
                ('abouttextf', models.TextField()),
                ('abouttextg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactbuilding', models.CharField(max_length=60)),
                ('contactcountry', models.CharField(max_length=60)),
                ('contactphone', models.CharField(max_length=60)),
                ('contactemail', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventimg1', models.FileField(upload_to='media')),
                ('eventtxt1', models.CharField(max_length=60)),
                ('eventimg2', models.FileField(upload_to='media')),
                ('eventtxt2', models.CharField(max_length=60)),
                ('eventimg3', models.FileField(upload_to='media')),
                ('eventtxt3', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutimg', models.FileField(upload_to='media')),
                ('abouttitle', models.CharField(max_length=60)),
                ('aboutpara1', models.TextField()),
                ('aboutpara2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogimg1', models.FileField(upload_to='media')),
                ('blogheading1', models.CharField(max_length=60)),
                ('blogtext1', models.CharField(max_length=60)),
                ('blogdate1', models.CharField(max_length=60)),
                ('blogurl1', models.URLField()),
                ('blogimg2', models.FileField(upload_to='media')),
                ('blogheading2', models.CharField(max_length=60)),
                ('blogtext2', models.CharField(max_length=60)),
                ('blogdate2', models.CharField(max_length=60)),
                ('blogurl2', models.URLField()),
                ('blogimg3', models.FileField(upload_to='media')),
                ('blogheading3', models.CharField(max_length=60)),
                ('blogtext3', models.CharField(max_length=60)),
                ('blogdate3', models.CharField(max_length=60)),
                ('blogurl3', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeLanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landingbackground', models.FileField(upload_to='media')),
                ('landinglogo', models.FileField(upload_to='images')),
                ('landingheading1', models.CharField(max_length=100)),
                ('landingtext1', models.TextField()),
                ('landingheading2', models.CharField(max_length=100)),
                ('landingtext2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeShows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showdate', models.CharField(max_length=60)),
                ('showtitle', models.CharField(max_length=120)),
                ('showhost', models.CharField(max_length=60)),
                ('eattime', models.CharField(max_length=60)),
                ('cattime', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showimg1', models.FileField(upload_to='media')),
                ('showtitle1', models.CharField(max_length=60)),
                ('showperiod1', models.CharField(max_length=60)),
                ('showtime1', models.CharField(max_length=60)),
                ('showabout1', models.TextField()),
                ('showurl1', models.URLField()),
                ('showimg2', models.FileField(upload_to='media')),
                ('showtitle2', models.CharField(max_length=60)),
                ('showperiod2', models.CharField(max_length=60)),
                ('showtime2', models.CharField(max_length=60)),
                ('showabout2', models.TextField()),
                ('showurl2', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffimg1', models.FileField(upload_to='media')),
                ('staffname1', models.CharField(max_length=60)),
                ('stafftitle1', models.CharField(max_length=60)),
                ('staffimg2', models.FileField(upload_to='media')),
                ('staffname2', models.CharField(max_length=60)),
                ('stafftitle2', models.CharField(max_length=60)),
                ('staffimg3', models.FileField(upload_to='media')),
                ('staffname3', models.CharField(max_length=60)),
                ('stafftitle3', models.CharField(max_length=60)),
                ('staffimg4', models.FileField(upload_to='media')),
                ('staffname4', models.CharField(max_length=60)),
                ('stafftitle4', models.CharField(max_length=60)),
                ('staffimg5', models.FileField(upload_to='media')),
                ('staffname5', models.CharField(max_length=60)),
                ('stafftitle5', models.CharField(max_length=60)),
                ('staffimg6', models.FileField(upload_to='media')),
                ('staffname6', models.CharField(max_length=60)),
                ('stafftitle6', models.CharField(max_length=60)),
            ],
        ),
    ]