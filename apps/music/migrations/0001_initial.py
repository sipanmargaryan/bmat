# Generated by Django 2.2.10 on 2020-06-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('contributors', models.CharField(max_length=150)),
                ('iswc', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
