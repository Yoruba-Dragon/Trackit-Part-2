# Generated by Django 5.1.3 on 2024-12-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='intesity',
            field=models.IntegerField(default=0),
        ),
    ]
