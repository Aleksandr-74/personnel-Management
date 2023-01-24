from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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
            citi = form.cleaned_data["citi"]
            foreman = form.cleaned_data["foreman"]
            worker = form.cleaned_data["mechanic"]
            foreman = Worker.objects.get(name_worker=foreman)
            worker = Worker.objects.get(name_worker=worker)
            brigade = Brigade.objects.create(сiti=citi, foreman=foreman)
            brigade.workers.add(worker)
            # return reverse('home')
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
    workers = [i for i in Brigade.objects.get(pk=brigade_id).workers.all()]
    data = {
        'citi': brigade.сiti,
        'foreman': brigade.foreman,
    }

    if len(workers) > 1:
        for worker in workers:
            data.update({'mechanic', worker.name_worker})
    else:
        data.update({'mechanic': workers[0]})

    form = UserBrigade(data)

    context = {
        'form': form,
        'brigade': brigade,
        'workers': workers,
    }


    return render(request, "Management_app/card_brigade.html", context=context)

