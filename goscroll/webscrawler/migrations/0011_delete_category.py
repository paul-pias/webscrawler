# Generated by Django 4.0 on 2021-12-29 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrawler', '0010_remove_data_categories_data_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
