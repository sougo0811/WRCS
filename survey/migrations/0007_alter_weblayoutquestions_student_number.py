# Generated by Django 4.1.2 on 2022-12-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_alter_weblayoutquestions_question_eighth_raspberrypi_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='student_number',
            field=models.IntegerField(default=9999999),
        ),
    ]
