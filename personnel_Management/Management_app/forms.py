from django import forms
from django.forms import ModelForm
from Management_app.models import Status, Role, Worker, Object_application, Brigade



class UserBrigade(ModelForm):
    """ Форма формирования бригады"""

    citi = forms.CharField(label="Город", widget=forms.TextInput(
        attrs={
            'class': 'form-control'
            }
    ))

    foreman = forms.ModelChoiceField(label='Бригадир',
        queryset=Worker.objects.filter(roles='Мастер'),
        widget=forms.Select(
            attrs={
                'class': 'form-select'
                }
    ))

    workers = forms.ModelMultipleChoiceField(label='Mexаник', queryset=Worker.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }))

    class Meta:
        model = Brigade
        fields = ('citi', 'foreman', 'workers')


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

    roles = forms.ChoiceField(label='Роль', choices=Role.choices,
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