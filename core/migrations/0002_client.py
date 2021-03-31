# Generated by Django 3.1.7 on 2021-03-29 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last_name')),
                ('email', models.EmailField(max_length=100, verbose_name='e-mail')),
            ],
        ),
    ]