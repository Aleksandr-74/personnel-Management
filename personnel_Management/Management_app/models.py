import datetime

from django.urls import reverse

from django.db import models


class Role(models.TextChoices):
    A = "selected", '-----'
    FOREMAN = 'Мастер', 'Мастер'
    MECHANIC = 'Механик', 'Механик'


class Worker(models.Model):
    roles = models.CharField(max_length=100, choices=Role.choices)
    name = models.CharField(max_length=150, db_index=True, verbose_name='Имя сотрудника')

    def __str__(self):
        return f'{self.roles}: {self.name}'

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse("worker", kwargs={"worker_id": self.pk})


class Brigade(models.Model):

    citi = models.CharField(
        max_length=150, verbose_name='Город'
    )

    foreman = models.ForeignKey(
        to='Worker', on_delete=models.PROTECT,
        blank=False, null=True,
        related_name='foreman', verbose_name="Мастер"
    )
    workers = models.ManyToManyField(to='Worker', verbose_name='Сотрудники', related_name='brigade')

    def __str__(self):
        return self.citi

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def get_absolute_url(self):
        return reverse("brigade", kwargs={"brigade_id": self.pk})



"""Объект"""

class TypeWorks(models.TextChoices):
    """Тип работ"""

    A = "selected", '-----'
    SERVICE = 'SERVICE', 'Техническое обслуживание'
    REPAIR = 'REPAIR', 'Ремонт'
    INSTALLATION = 'INSTALLATION', 'Монтаж'
    ASSEMBLY = 'ASSEMBLY', 'Сборка'


class Status(models.TextChoices):
    """ Статус объекта"""

    A = "selected", '-----'
    NEWS = "Новый", "Новый"
    LAUNCHED_INTO_WORK = "Запущен в работу", "Запущен в работу"
    PAUSE = "Пауза", "Пауза"
    COMPLETED = "Завершен", "Завершен"



class Objectes(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Имя объекта')
    place_work = models.CharField(max_length=150, verbose_name='Место работ')
    description = models.TextField(verbose_name="Описание работ")
    type_works = models.CharField(max_length=100, choices=TypeWorks.choices, verbose_name='Тип работ')
    status_work = models.CharField(max_length=100, choices=Status.choices, verbose_name='Статус работ')
    brigades = models.ForeignKey(to="Brigade", on_delete=models.PROTECT, verbose_name="Бригада")

    def __str__(self):
        return f"{self.name}, статус: {self.status_work}"

    def get_absolute_url(self):
        return reverse("objecte", kwargs={"objectes_id": self.pk})



# class ObjectBrigade(models.Model):
#     brigade = models.ForeignKey('Brigade', on_delete=models.CASCADE)
#     objecte = models.ForeignKey('Object_application', on_delete=models.CASCADE)
#     date_start = models.DateField(null=True, blank=True)
