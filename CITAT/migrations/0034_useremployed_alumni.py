# Generated by Django 3.1.7 on 2022-03-10 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0033_auto_20220311_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='useremployed',
            name='alumni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CITAT.alumni'),
        ),
    ]
