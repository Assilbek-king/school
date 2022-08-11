# Generated by Django 4.0.4 on 2022-04-20 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_lesson_teacher_alter_lesson_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'doljnost': 1}, on_delete=django.db.models.deletion.CASCADE, to='main.infoteacher'),
        ),
        migrations.AlterField(
            model_name='sinf',
            name='leader',
            field=models.ForeignKey(limit_choices_to={'doljnost': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='rahbar', to='main.infoteacher'),
        ),
        migrations.AlterField(
            model_name='sinf',
            name='tar1',
            field=models.ForeignKey(limit_choices_to={'doljnost': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='tarbiyachi1', to='main.infoteacher'),
        ),
        migrations.AlterField(
            model_name='sinf',
            name='tar2',
            field=models.ForeignKey(limit_choices_to={'doljnost': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='tarbiyachi2', to='main.infoteacher'),
        ),
    ]
