from django import forms

from Management_app.models import Status, Role, Worker


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
            'class': 'input_form'
        }))

    foreman = forms.ChoiceField(label='Бригадир',
        choices=tuple(Worker.objects.filter(roles_id=1).values_list("id", "name_worker")),
        widget=forms.Select(
            attrs={
                'class': 'input_form'
            }))

    mechanic = forms.ChoiceField(label='Mexаник',
        choices=tuple(Worker.objects.all().values_list("pk", "name_worker")),
        widget=forms.Select(attrs={'class': 'input_form'}))




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


class UserWorker(forms.Form):
    """ Регистрация сотрудник в БД"""

    roles = forms.ChoiceField(label='Роль',
        choices=tuple(Role.objects.all().values_list("id", "role")),
        widget=forms.Select(
            attrs={
                'class': 'input_form'
            }))

    name_worker = forms.CharField(label='Имя', max_length=256, widget=forms.TextInput(
        attrs={
            'class': 'input_form'
        }))

    class Meta:
        model = Worker
        fields = ('roles', 'name_worker')