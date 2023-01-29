from rest_framework import generics
# from django.http import Response
from django.shortcuts import render, get_object_or_404


from Management_app.forms import UserBrigade, UserWorker, UserRequest
from Management_app.models import Worker, Brigade
from Management_app.serializers import WorkerSerializer, BrigadeSerializer


class BrigadesAPIList(generics.ListCreateAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()






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
            print(roles, name_worker)
            Worker.objects.create(roles=roles, name_worker=name_worker)
    #         return reverse('home')
    return render(request, "Management_app/content.html", context=context)



def BrigadeFormView(request):
    form = UserBrigade
    context = {
        "title": "Регистрация бригады",
        "form": form
    }
    if request.method == "POST":
        form = UserBrigade(request.POST)
        if form.is_valid():
            # data = form.cleaned_data[" "]
            citi = form.cleaned_data["citi"]
            foreman = form.cleaned_data["foreman"]
            worker = form.cleaned_data["mechanic"]
            foreman = Worker.objects.get(name_worker=foreman)
            worker = Worker.objects.get(name_worker=worker)
            brigade = Brigade.objects.create(citi=citi, foreman=foreman)
            brigade.workers.add(worker)
            # return reverse('home')

    return render(request, "Management_app/brigade.html", context=context)


def FormObject(request):
    form = UserRequest
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
    workers = [i for i in Brigade.objects.get(pk=brigade_id).workers.all()]
    data = {
        'citi': brigade.citi,
        'foreman': brigade.foreman,
    }
    for worker in workers:
        data.update({'mechanic': worker})

    form = UserBrigade(data)
    context = {
        'form': form,
        'brigade': brigade,
        'workers': workers,
        'title': 'Информация о бригаде'
    }
    return render(request, "Management_app/card_brigade.html", context=context)

