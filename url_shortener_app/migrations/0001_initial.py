# Generated by Django 3.1.4 on 2020-12-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LongToShort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.URLField(max_length=250)),
                ('shorturl', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]