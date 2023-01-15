from django import forms

from Management_app.models import Status, Role, Employee


class User_role(forms.Form):
    """Создания ролей сотрудников"""

    name_role = forms.CharField(label="Роль", widget=forms.TextInput(
        attrs={'class': 'input_form', 'placeholder': 'Роль'}))

    class Meta:
        model = Role
        fields = ("name_role")


class User_brigade(forms.Form):
    """ Форма формирования бригады"""

    citi = forms.CharField(label="Город", widget=forms.TextInput(
        attrs={'class': 'input_form'}))

    foreman = forms.ChoiceField(label='Бригадир',
        choices=tuple(Employee.objects.filter(roles_id=1).values_list("id", "name_employee")),
        widget=forms.Select(attrs={'class': 'input_form'}))

    mechanic = forms.ChoiceField(label='Mexаник',
        choices=tuple(Employee.objects.filter(roles_id=2).values_list("id", "name_employee")),
        widget=forms.Select(attrs={'class': 'input_form'}))




class Object_status(forms.Form):
    """Форма для создания статуса объета"""

    name_staus = forms.CharField(label='Статус', max_length=256,
        widget=forms.TextInput(attrs={'class': 'input_form', 'placeholder': 'Статус'}))

    class Meta:
        model = Status
        fields = ('name_staus')


class User_Employee(forms.Form):
    """ Регистрация сотрудник в БД"""

    name_employee = forms.CharField(label='Имя', max_length=256, widget=forms.TextInput(
        attrs={'class': 'input_form'}))

    id_role = forms.ChoiceField(label='Роль',
        choices=tuple(Role.objects.all().values_list("id", "role")),
        widget=forms.Select(
            attrs={
                'class': 'input_form'}))

    class Meta:
        model = Employee
        fields = ('role_id', 'name_employee')