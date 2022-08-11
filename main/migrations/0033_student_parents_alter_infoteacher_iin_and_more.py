# Generated by Django 4.0.4 on 2022-05-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_remove_student_parent_birth_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parents',
            field=models.ManyToManyField(blank=True, null=True, to='main.student_parent'),
        ),
        migrations.AlterField(
            model_name='infoteacher',
            name='iin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='iin',
            field=models.IntegerField(default=0),
        ),
    ]