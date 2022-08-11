# Generated by Django 4.0.4 on 2022-04-21 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_infoteacher_number2_alter_infoteacher_doljnost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoteacher',
            name='doljnost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.doljnost'),
        ),
        migrations.AlterField(
            model_name='infoteacher',
            name='middle_name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]