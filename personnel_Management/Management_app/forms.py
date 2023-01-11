from django import forms

from Management_app.models import Brigade

class User_brigade(forms.Forms):
    pass

class Meta:
    model = Brigade
    fields = ("username", "password1", "password2")