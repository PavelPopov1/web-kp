# Generated by Django 3.2.8 on 2021-12-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211207_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
