# Generated by Django 5.0.3 on 2024-04-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneByteFood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
