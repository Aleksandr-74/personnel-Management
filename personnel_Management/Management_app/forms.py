from django import forms
from django.forms import ModelForm
from Management_app.models import Status, Role, Worker, Object_application


class UserRole(forms.Form):
    """Создания ролей сотрудников"""

    name_role = forms.CharField(label="Роль", widget=forms.TextInput(
        attrs={
            'class': 'input_form',
            'placeholder': 'Роль'
        }))

    class Meta:
        model = Role
        fields = ("name_role")


class UserBrigade(forms.Form):
    """ Форма формирования бригады"""

    citi = forms.CharField(label="Город", widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }))

    foreman = forms.ChoiceField(label='Бригадир',
        choices=tuple(Worker.objects.filter(roles_id=1).values_list("id", "name_worker")),
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }))

    mechanic = forms.ChoiceField(label='Mexаник',
        choices=tuple(Worker.objects.all().values_list("pk", "name_worker")),
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }))




class Object_status(forms.Form):
    """Форма для создания статуса объета"""

    name_staus = forms.CharField(label='Статус', max_length=256,
        widget=forms.TextInput(
            attrs={
                'class': 'input_form',
                'placeholder': 'Статус'
            }))

    class Meta:
        model = Status
        fields = ('name_staus')


class UserWorker(ModelForm):
    """ Регистрация сотрудник в БД"""

    roles = forms.ChoiceField(label='Роль',
        choices=tuple(Role.objects.all().values_list("id", "role")),
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }))

    name_worker = forms.CharField(label='Имя', max_length=256, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }))

    class Meta:
        model = Worker
        fields = ('roles', 'name_worker')


class UserRequest(ModelForm):
    class Meta:
        model =Object_application
        fields = ('name', 'place_work', 'description', 'type_works',
                  'status_work', 'start_time', 'finishing_time', 'brigades')