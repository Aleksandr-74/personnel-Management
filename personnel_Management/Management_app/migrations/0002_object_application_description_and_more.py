# Generated by Django 4.1.5 on 2023-01-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='object_application',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание работ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object_application',
            name='finishing_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время окончания работ'),
        ),
        migrations.AddField(
            model_name='object_application',
            name='name',
            field=models.CharField(db_index=True, default=1, max_length=150, verbose_name='Имя объекта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object_application',
            name='place_work',
            field=models.CharField(default=1, max_length=150, verbose_name='Место работ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object_application',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время начала работ'),
        ),
        migrations.AddField(
            model_name='object_application',
            name='status_work',
            field=models.CharField(choices=[], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object_application',
            name='type_works',
            field=models.CharField(choices=[('SERVICE', 'Техническое обслуживание'), ('REPAIR', 'Ремонт'), ('INSTALLATION', 'Монтаж'), ('ASSEMBLY', 'Сборка')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brigade',
            name='foreman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forema', to='Management_app.worker', verbose_name='Бригадир'),
        ),
        migrations.AlterField(
            model_name='brigade',
            name='workers',
            field=models.ManyToManyField(related_name='brigades', to='Management_app.worker', verbose_name='Сотрудники'),
        ),
        migrations.CreateModel(
            name='ObjectBrigade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(blank=True, null=True)),
                ('brigade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management_app.brigade')),
                ('objecte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management_app.object_application')),
            ],
        ),
        migrations.AddField(
            model_name='object_application',
            name='brigades',
            field=models.ManyToManyField(through='Management_app.ObjectBrigade', to='Management_app.brigade'),
        ),
    ]
