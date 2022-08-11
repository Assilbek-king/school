# Generated by Django 4.0.4 on 2022-04-19 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_doljnost_infoteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sinf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('stage', models.IntegerField(max_length=2)),
                ('symbol', models.CharField(max_length=2)),
                ('amount_student', models.IntegerField(max_length=2)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rahbar', to='main.infoteacher')),
                ('tar1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarbiyachi1', to='main.infoteacher')),
                ('tar2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarbiyachi2', to='main.infoteacher')),
            ],
        ),
    ]
