# Generated by Django 4.1 on 2022-09-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_gallery_remove_blog_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='food/')),
                ('name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=200)),
                ('social_media', models.CharField(choices=[('instagram', 'instagram'), ('linkedin', 'linkedin'), ('google', 'google')], max_length=10)),
            ],
        ),
    ]
