# Generated by Django 3.1.2 on 2020-10-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='Photo'),
            preserve_default=False,
        ),
    ]
