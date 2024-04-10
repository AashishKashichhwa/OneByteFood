# Generated by Django 5.0.3 on 2024-04-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneByteFood', '0003_alter_reservation_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('staff_status', models.BooleanField(default=False)),
            ],
        ),
    ]
