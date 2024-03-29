# Generated by Django 4.1.7 on 2023-04-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_member_email_alter_member_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='city_en',
            field=models.CharField(default='', max_length=255, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='job',
            name='details_en',
            field=models.TextField(default='', verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='job',
            name='name_en',
            field=models.CharField(default='', max_length=255, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='job',
            name='wage_en',
            field=models.CharField(default='', max_length=255, verbose_name='Wage'),
        ),
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='job',
            name='details',
            field=models.TextField(verbose_name='Детали'),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='job',
            name='wage',
            field=models.CharField(max_length=255, verbose_name='Зарплата'),
        ),
    ]
