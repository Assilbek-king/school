# Generated by Django 4.0.4 on 2022-04-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_infoteacher_birth_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoteacher',
            name='birth_day',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='infoteacher',
            name='data_prikaz',
            field=models.DateTimeField(),
        ),
    ]
