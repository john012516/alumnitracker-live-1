# Generated by Django 4.0.2 on 2022-03-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0021_auto_20220306_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]