from django.db import models


class Role(models.Model):
    name_role = models.CharField(max_length=150, db_index=True, verbose_name='Роль')

    def __str__(self):
        return self.name_role

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Авторы"


class Employee(models.Model):
    id_role = models.ForeignKey('Role', on_delete=models.PROTECT, verbose_name='Роль')
    name_employee = models.CharField(max_length=150, db_index=True, verbose_name='Имя сотрудника')


class Brigade(models.Model):
    id_employee = models.ForeignKey('Employee', on_delete=models.PROTEC, verbose_name='Сотрудник')

    def __str__(self):
        return self.id_employee






class Status(models.Model):
    pass


class Object_application(models.Model):
    pass
