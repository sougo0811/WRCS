# Generated by Django 4.1.2 on 2022-12-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_wrcs_sumple_delete_surveytest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wrcs_sumple',
            name='RaspberryPi_ID',
            field=models.IntegerField(),
        ),
    ]
