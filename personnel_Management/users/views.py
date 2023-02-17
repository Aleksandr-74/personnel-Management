from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from users.form import RegisterForm, AuthorizationForm


class Register(View):
    temlate_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': RegisterForm()
        }
        return render(request, self.temlate_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            users = authenticate(username=username, password=password)
            login(request, users)
            return redirect('/')
        context = {
            'form': form
        }

        return render(request, self.temlate_name, context)


class LoginUsers(LoginView):
    template_name = "registration/login.html"
    form_class = AuthorizationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация сотрудника"
        return context