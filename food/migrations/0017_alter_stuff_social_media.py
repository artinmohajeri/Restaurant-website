# Generated by Django 4.1 on 2022-09-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0016_alter_stuff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='social_media',
            field=models.ManyToManyField(related_name='stuff_media', to='food.socialmedia'),
        ),
    ]
