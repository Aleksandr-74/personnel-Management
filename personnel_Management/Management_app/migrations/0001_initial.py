<<<<<<< HEAD
# Generated by Django 4.1.5 on 2023-01-27 16:04
=======
# Generated by Django 4.1.5 on 2023-01-25 03:54
>>>>>>> origin/authorization

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('citi', models.CharField(max_length=150, verbose_name='Город')),
=======
                ('сiti', models.CharField(max_length=150, verbose_name='Город')),
>>>>>>> origin/authorization
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Object_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Имя объекта')),
                ('place_work', models.CharField(max_length=150, verbose_name='Место работ')),
                ('description', models.TextField(verbose_name='Описание работ')),
                ('type_works', models.CharField(choices=[('SERVICE', 'Техническое обслуживание'), ('REPAIR', 'Ремонт'), ('INSTALLATION', 'Монтаж'), ('ASSEMBLY', 'Сборка')], max_length=100)),
                ('status_work', models.CharField(choices=[], max_length=100)),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Время начала работ')),
                ('finishing_time', models.DateTimeField(blank=True, null=True, verbose_name='Время окончания работ')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(choices=[('selected', '-----'), ('Мастер', 'Мастер'), ('Механик', 'Механик')], max_length=100)),
                ('name_worker', models.CharField(db_index=True, max_length=150, verbose_name='Имя сотрудника')),
            ],
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
            field=models.ManyToManyField(through='Management_app.ObjectBrigade', to='Management_app.brigade', verbose_name='Бригада'),
        ),
        migrations.AddField(
            model_name='brigade',
            name='foreman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreman', to='Management_app.worker', verbose_name='Бригадир'),
        ),
        migrations.AddField(
            model_name='brigade',
            name='workers',
            field=models.ManyToManyField(related_name='brigades', to='Management_app.worker', verbose_name='Сотрудники'),
        ),
    ]
