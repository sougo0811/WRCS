# Generated by Django 4.1.2 on 2022-12-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_alter_weblayoutquestions_question_ninth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_eighth_RaspberryPi_ID',
            field=models.BooleanField(default=False, null=True, verbose_name='ソートラズパイID'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_eighth_altitude',
            field=models.BooleanField(default=False, null=True, verbose_name='ソート高度'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_eighth_date',
            field=models.BooleanField(default=False, null=True, verbose_name='ソート取得日時'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_eighth_future_temperature',
            field=models.BooleanField(default=False, null=True, verbose_name='ソート今後気温'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_eighth_now_temperature',
            field=models.BooleanField(default=False, null=True, verbose_name='ソート現在気温'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_eighth_water_high',
            field=models.BooleanField(default=False, null=True, verbose_name='ソート水位'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_eighth_water_temperature',
            field=models.BooleanField(default=False, null=True, verbose_name='ソート水温'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_fifth',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルターは必要か'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_first_sumple1',
            field=models.BooleanField(default=False, null=True, verbose_name='サンプルページ1が見やすかった'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_first_sumple2',
            field=models.BooleanField(default=False, null=True, verbose_name='サンプルページ2が見やすかった'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_first_sumple3',
            field=models.BooleanField(default=False, null=True, verbose_name='サンプルページ3が見やすかった'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_fourth',
            field=models.IntegerField(default=0, null=True, verbose_name='一番貯水槽の稼働状況を見比べやすかったサンプル'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_ninth',
            field=models.TextField(max_length=256, null=True, verbose_name='意見'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_second',
            field=models.IntegerField(default=0, null=True, verbose_name='1番見やすかったサンプル'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_seventh',
            field=models.BooleanField(default=False, null=True, verbose_name='ソートは必要か'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_RaspberryPi_ID',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルターラズパイID'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_RaspberryPi_point',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルターラズパイ場所'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_altitude',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター高度'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_date',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター取得日時'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_future_temperature',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター今後気温'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_future_weather',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター今後天気'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_is_water_in',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター散水状況'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_is_water_out',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター吸水状況'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_now_temperature',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター現在気温'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_now_weather',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター現在天気'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_water_high',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター水位'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_sixth_water_temperature',
            field=models.BooleanField(default=False, null=True, verbose_name='フィルター水温'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_third_sumple1',
            field=models.BooleanField(default=False, null=True, verbose_name='サンプルページ1が貯水槽の稼働状況を見比べやすかった'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_third_sumple2',
            field=models.BooleanField(default=False, null=True, verbose_name='サンプルページ2が貯水槽の稼働状況を見比べやすかった'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='question_third_sumple3',
            field=models.BooleanField(default=False, null=True, verbose_name='サンプルページ3が貯水槽の稼働状況を見比べやすかった'),
        ),
        migrations.AlterField(
            model_name='weblayoutquestions',
            name='student_number',
            field=models.IntegerField(unique=True, verbose_name='学籍番号'),
        ),
    ]
