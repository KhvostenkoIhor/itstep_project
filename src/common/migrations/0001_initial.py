# Generated by Django 2.2.7 on 2020-11-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images\\')),
                ('is_avatar', models.BooleanField(default=False)),
            ],
        ),
    ]
