# Generated by Django 4.0.3 on 2022-04-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_ashiqsabaq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(max_length=5)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
    ]