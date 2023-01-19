from django.shortcuts import render

from Management_app.forms import UserBrigade, UserWorker
from Management_app.models import Worker, Brigade


def home(request):
    workers = Worker.objects.all()
    brigabes = Brigade.objects.all()
    context = {
        "workers": workers,
        "brigades": brigabes
    }
    return render(request, "Management_app/home.html", context=context)

def FormEmployee(request):
    form = UserWorker
    context = {
        "form": form
    }
    if request.method == "POST":
        form = UserWorker(request.POST)
        if form.is_valid():
            name_worker = form.cleaned_data["name_worker"]
            roles = form.cleaned_data["roles"]
            print(roles, name_worker)
            worker = Worker.objects.create(roles_id=roles, name_worker=name_worker)
    return render(request, "Management_app/content.html", context=context)


def FormBrigade(request):
    form = UserBrigade
    context = {
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

    return render(request, "Management_app/brigade.html", context=context)


def InfoBrigade(request):
    print(request)
    brigabes = Brigade.objects.filter(id == "pk")
    print(brigabes)
