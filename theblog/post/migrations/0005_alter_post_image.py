# Generated by Django 3.2.9 on 2021-11-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
