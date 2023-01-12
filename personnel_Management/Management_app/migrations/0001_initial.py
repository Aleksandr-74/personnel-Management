# Generated by Django 4.1.5 on 2023-01-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_role', models.CharField(db_index=True, max_length=150, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_staus', models.CharField(max_length=256, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_employee', models.CharField(db_index=True, max_length=150, verbose_name='Имя сотрудника')),
                ('id_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Management_app.role', verbose_name='Роль')),
            ],
        ),
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Management_app.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
