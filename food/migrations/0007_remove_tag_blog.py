# Generated by Django 4.1 on 2022-09-14 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_tag_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='blog',
        ),
    ]
