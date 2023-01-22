from django.shortcuts import render, get_object_or_404
from django.urls import reverse, resolve
from django.http import HttpResponse
from Management_app.forms import UserBrigade, UserWorker, UserRequest
from Management_app.models import Worker, Brigade


def home(request):
    workers = Worker.objects.all()
    brigabes = Brigade.objects.all()
    context = {
        "title": "Главная страница",
        "workers": workers,
        "brigades": brigabes
    }
    return render(request, "Management_app/home.html", context=context)


def FormWorker(request):
    form = UserWorker
    context = {
        "title": "Регистрация сотрудника",
        "form": form
    }
    if request.method == "POST":
        form = UserWorker(request.POST)
        if form.is_valid():
            name_worker = form.cleaned_data["name_worker"]
            roles = form.cleaned_data["roles"]
            print(roles, name_worker)
            Worker.objects.create(roles_id=roles, name_worker=name_worker)
            return reverse('home')
    return render(request, "Management_app/content.html", context=context)


def FormBrigade(request):
    form = UserBrigade
    context = {
        "title": "Регистрация бригады",
        "form": form
    }
    if request.method == "POST":
        form = UserBrigade(request.POST)
        if form.is_valid():
            citi = form.cleaned_data["citi"]
            foreman_id = int(form.cleaned_data["foreman"])
            worker_id = int(form.cleaned_data["mechanic"])
            worker = Worker.objects.get(pk=worker_id)
            brigade = Brigade.objects.create(сiti=citi, foreman_id=foreman_id)
            brigade.workers.add(worker)
            return reverse('home')
    return render(request, "Management_app/brigade.html", context=context)


def FormObject(request):
    form = UserRequest
    print(form)
    context = {
        'title': 'Регистрация объекта',
        "form": form
    }
    return render(request, "Management_app/request.html", context=context)


def InfoWorker(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    return HttpResponse(f"{worker}")



def InfoBrigade(request, brigade_id):
    brigade = get_object_or_404(Brigade, pk=brigade_id)
    return HttpResponse(f"{brigade}")
