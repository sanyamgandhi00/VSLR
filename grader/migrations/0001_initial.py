# Generated by Django 3.1.7 on 2021-02-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sample_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('college', models.TextField()),
                ('code', models.CharField(max_length=255)),
                ('sample', models.FileField(upload_to='sample')),
            ],
        ),
        migrations.CreateModel(
            name='student_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('answer', models.FileField(upload_to='answer')),
            ],
        ),
    ]
