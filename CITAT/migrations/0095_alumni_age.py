# Generated by Django 3.1.7 on 2022-04-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0094_auto_20220411_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='Age',
            field=models.CharField(max_length=200, null=True),
        ),
    ]