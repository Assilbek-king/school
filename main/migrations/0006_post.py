# Generated by Django 4.0.3 on 2022-04-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_calculate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField()),
                ('views', models.IntegerField()),
                ('logo', models.ImageField(upload_to='upload')),
                ('mini_description', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('author', models.CharField(default='Admin', max_length=300)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]