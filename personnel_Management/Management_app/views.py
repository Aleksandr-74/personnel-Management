from rest_framework import generics
from django.shortcuts import render, get_object_or_404

from Management_app.forms import UserBrigade, UserWorker, UserRequest
from Management_app.models import Worker, Brigade
from Management_app.serializers import WorkerSerializer, BrigadeSerializer


class BrigadesAPIList(generics.ListCreateAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class BrigadeAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class WorkerAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


def home(request):
    workers = Worker.objects.all()
    brigabes = Brigade.objects.all()
    context = {
        "title": "Главная страница",
        "workers": workers,
        "brigades": brigabes
    }
    return render(request, "Management_app/home.html", context=context)


def WorkerFormView(request):
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
            Worker.objects.create(roles=roles, name_worker=name_worker)
    #         return reverse('home')
    return render(request, "Management_app/content.html", context=context)



def BrigadeFormView(request):
    form = UserBrigade

    def Updates(worker):
        Worker.objects.filter(name_worker=worker).update(added_to_composition=1)
        print(worker.added_to_composition)
        return worker

    context = {
        "title": "Регистрация бригады",
        "form": form
    }
    if request.method == "POST":
        form = UserBrigade(request.POST)
        if form.is_valid():
            citi = form.cleaned_data["citi"]
            foreman = form.cleaned_data["foreman"]
            Updates(foreman)
            brigade = Brigade.objects.create(
                citi=citi, foreman=foreman)
            for worker in form.cleaned_data['workers']:
                print(worker)
                Updates(worker)
                brigade.workers.add(worker)

    return render(request, "Management_app/brigade.html", context=context)


def FormObject(request):
    form = UserRequest
    context = {
        'title': 'Регистрация объекта',
        "form": form
    }
    return render(request, "Management_app/request.html", context=context)


def InfoWorker(request, worker_id):
    return render(request, "Management_app/card_worker.html")


def InfoBrigade(request, brigade_id):
    brigade = get_object_or_404(Brigade, pk=brigade_id)
    workers = [i for i in Brigade.objects.get(pk=brigade_id).workers.all()]
    data = {
        'citi': brigade.citi,
        'foreman': brigade.foreman,
        'workers': workers
    }

    form = UserBrigade(data)
    context = {
        'form': form,
        'brigade': brigade,
        'workers': workers,
        'title': 'Информация о бригаде'
    }

    return render(request, "Management_app/card_brigade.html", context=context)

