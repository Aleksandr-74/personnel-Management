from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=150, db_index=True, verbose_name='Роль')

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

class Worker(models.Model):
    roles = models.ForeignKey('Role', on_delete=models.PROTECT, verbose_name='Роль')
    name_worker = models.CharField(max_length=150, db_index=True, verbose_name='Имя сотрудника')

    def __str__(self):
        return self.name_worker

    class Meta:
        pass


class Brigade(models.Model):
    сiti = models.CharField(max_length=150, verbose_name='Город')
    foreman = models.ForeignKey("Worker", related_name='forema', on_delete=models.PROTECT, verbose_name="Бригадир")
    workers = models.ManyToManyField("Worker", related_name='brigades', verbose_name="Сотрудники")

    def __str__(self):
        return self.сiti

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"



"""Объект"""


class Status(models.TextChoices):
    """ Статус объекта"""
    pass



class Object_application(models.Model):
    pass
