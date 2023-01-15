from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=150, db_index=True, verbose_name='Роль')

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Employee(models.Model):
    roles = models.ForeignKey('Role', on_delete=models.PROTECT, verbose_name='Роль')
    name_employee = models.CharField(max_length=150, db_index=True, verbose_name='Имя сотрудника')

    def __str__(self):
        return self.name_employee

    class Meta:
        pass


class Brigade(models.Model):
    сiti = models.CharField(max_length=150, verbose_name='Город')
    employees = models.ManyToManyField("Employee", verbose_name="Сотрудники")

    def __str__(self):
        return self.Citi

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


# class BrigadeEmployee(models.Model):
#     employee_id = models.ForeignKey("Employee", on_delete=models.PROTECT, verbose_name='Сотрудник')
#     brigade_id = models.ForeignKey("Brigade", on_delete=models.PROTECT)


"""Объект"""


class Status(models.Model):
    name_staus = models.CharField(max_length=256, verbose_name='Статус')

    def __str__(self):
        return self.name_staus

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Object_application(models.Model):
    pass
