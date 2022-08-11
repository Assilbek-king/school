# Generated by Django 4.0.3 on 2022-04-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_delete_blog1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('info', models.CharField(max_length=500)),
                ('logo', models.ImageField(upload_to='upload')),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]