from django import forms

from Management_app.models import Status, Role


class User_role(forms.Form):
    """Создания ролей сотрудников"""

    name_role = forms.CharField(label="Роль", widget=forms.TextInput(
        attrs={'class': 'input_form',
                'placeholder': 'Роль'}))

    class Meta:
        model = Role
        fields = ("name_role")


class User_brigade(forms.Form):
    """ Форма формирования бригады"""

    foreman = forms.CharField(label='Бригадир', widget=forms.Select(
            attrs={'class': 'input_form',
                   'placeholder': 'Бригадир'}))

    mechanic = forms.CharField(label='Mexаник', widget=forms.Select(
            attrs={
                'class': 'input_form',
                'placeholder': 'Механик'}))


class Object_status(forms.Form):
    """Форма для создания статуса объета"""

    name_staus = forms.CharField(label='Статус', max_length=256, widget=forms.TextInput(
            attrs={'class': 'input_form',
                   'placeholder': 'Статус'}))
    class Meta:
        model = Status
        fields = ('name_staus')

