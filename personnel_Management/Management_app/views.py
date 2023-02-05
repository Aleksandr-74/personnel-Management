from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, FormView
from rest_framework import generics

from Management_app.forms import UserBrigade, UserWorker, UserObjects
from Management_app.models import Worker, Brigade, Objectes
from Management_app.serializers import WorkerSerializer, BrigadeSerializer


class BrigadeAPI(generics.RetrieveDestroyAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class WorkerAPI(generics.RetrieveDestroyAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class HomeListView(TemplateView):
    """Глваная страничка"""

    template_name = "Management_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workers'] = Worker.objects.all()
        context['brigades'] = Brigade.objects.all()
        context['objectes'] = Objectes.objects.all()
        context['title'] = "Главная страница"
        context['cat_selected'] = 0
        return context


class AddWorker(CreateView):
    """Добавление сотрудников"""

    template_name = "Management_app/content.html"
    form_class = UserWorker
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация сотрудника"
        context['cat_selected'] = 0
        return context

    def form_vaid(self, form):
        return super().form_valid(form)


class AddBrigade(CreateView):
    """Регистрация бригады"""

    template_name = "Management_app/brigade.html"
    form_class = UserBrigade
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация бригады"
        context['cat_selected'] = 0
        return context


class DetailWorker(DetailView):
    """Информация о сотруднике"""

    model = Worker
    field = ('roles', 'name')
    template_name = "Management_app/card_worker.html"
    pk_url_kwarg = 'worker_id'
    # success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о сотруднике"
        context['cat_selected'] = 0
        return context


class DatailBrigade(UpdateView, FormView):
    model = Brigade
    template_name = "Management_app/card_brigade.html"
    form_class = UserBrigade
    pk_url_kwarg = 'brigade_id'
    success_url = reverse_lazy('home')

    # workers = Brigade.objects.get(pk=brigade_id).worker.filter(roles='Механик')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о бригаде"
        context['workers'] = Brigade.objects.get(pk=1).workers.filter(roles='Механик')
        context['cat_selected'] = 0
        return context


class AddObject(CreateView):
    """Рeгистрация объета"""

    template_name = "Management_app/request.html"
    form_class = UserObjects
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация объекта"
        context['cat_selected'] = 0
        return context


class DataiObjects(UpdateView, FormView):
    """Информацмя о объекте"""

    model = Objectes
    template_name = "Management_app/card_objectes.html"
    fields = ('status_work',)
    pk_url_kwarg = 'objectes_id'
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о объекте"
        context['cat_selected'] = 0
        return context



