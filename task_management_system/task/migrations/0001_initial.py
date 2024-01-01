# Generated by Django 4.2.7 on 2024-01-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDescription', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='category.categorymodel')),
            ],
        ),
    ]