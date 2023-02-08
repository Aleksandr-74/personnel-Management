# Generated by Django 4.1.5 on 2023-02-07 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management_app', '0002_objectes_finishing_time_objectes_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectes',
            name='brigades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='object', to='Management_app.brigade', verbose_name='Бригада'),
        ),
        migrations.AlterField(
            model_name='objectes',
            name='finishing_time',
            field=models.DateField(blank=True, null=True, verbose_name='Время окончания работ'),
        ),
        migrations.AlterField(
            model_name='objectes',
            name='start_time',
            field=models.DateField(blank=True, null=True, verbose_name='Время начала работ'),
        ),
        migrations.AlterField(
            model_name='objectes',
            name='status_work',
            field=models.CharField(choices=[('Новый', 'Новый'), ('Запущен в работу', 'Запущен в работу'), ('Пауза', 'Пауза'), ('Завершен', 'Завершен')], default='Новый', max_length=100, verbose_name='Статус работ'),
        ),
    ]
