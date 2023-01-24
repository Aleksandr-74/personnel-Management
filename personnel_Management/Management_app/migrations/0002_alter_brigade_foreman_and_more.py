# Generated by Django 4.1.5 on 2023-01-24 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brigade',
            name='foreman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreman', to='Management_app.worker', verbose_name='Бригадир'),
        ),
        migrations.AlterField(
            model_name='object_application',
            name='brigades',
            field=models.ManyToManyField(through='Management_app.ObjectBrigade', to='Management_app.brigade', verbose_name='Бригада'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='roles',
            field=models.CharField(choices=[('selected', '-----'), ('Мастер', 'Мастер'), ('Механик', 'Механик')], max_length=100),
        ),
    ]
