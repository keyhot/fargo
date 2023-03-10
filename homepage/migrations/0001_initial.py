# Generated by Django 4.1.7 on 2023-03-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('wage', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото')),
                ('details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания вакансии')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки заявки')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
