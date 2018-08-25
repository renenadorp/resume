# Generated by Django 2.0.6 on 2018-08-25 10:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180817_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('descr', models.TextField(blank=True, null=True)),
                ('active', models.CharField(default='Y', max_length=1)),
                ('date_start', models.DateField(blank=True, default=datetime.datetime(2018, 8, 25, 10, 50, 28, 107677, tzinfo=utc))),
                ('date_end', models.DateField(blank=True, default=datetime.datetime(2018, 8, 25, 10, 50, 28, 107699, tzinfo=utc))),
                ('card_image', models.CharField(blank=True, default='education-card-default.jpg', max_length=100, null=True)),
                ('completed', models.BooleanField(default=True)),
                ('cv', models.ManyToManyField(to='app.CV')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='date_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 8, 25, 10, 50, 28, 103204, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 8, 25, 10, 50, 28, 104578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 8, 25, 10, 50, 28, 104550, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='education',
            name='person',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='app.Person'),
        ),
    ]