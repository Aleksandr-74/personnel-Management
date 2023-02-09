from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, FormView
from rest_framework import generics

from Management_app.forms import UserBrigade, UserWorker, UserObjects
from Management_app.models import Worker, Brigade, Objectes
from Management_app.serializers import WorkerSerializer, BrigadeSerializer, ObjectSeSerializer


class BrigadeAPI(generics.RetrieveDestroyAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class WorkerAPI(generics.RetrieveDestroyAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class AddObjectAPI(generics.CreateAPIView):
    serializer_class = ObjectSeSerializer
    queryset = Objectes.objects.all()

@method_decorator(login_required, name='dispatch')
class HomeListView(TemplateView):
    """Глваная страничка"""
    template_name = "Management_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workers'] = Worker.objects.all()
        context['brigades'] = Brigade.objects.all()
        context['objectes'] = Objectes.objects.all()
        context['title'] = "Главная страница"
        return context


'''Блок добавления в БД'''
@method_decorator(login_required, name='dispatch')
class AddWorker(CreateView):
    """Добавление сотрудников"""

    template_name = "Management_app/reg_worker.html"
    form_class = UserWorker
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация сотрудника"
        return context

    def form_vaid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AddBrigade(CreateView,  FormView):
    """Регистрация бригады"""

    template_name = "Management_app/brigade.html"
    form_class = UserBrigade
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация бригады"
        return context

@method_decorator(login_required, name='dispatch')
class AddObject(CreateView, FormView):
    """Рeгистрация объета"""

    template_name = "Management_app/reg_object.html"
    form_class = UserObjects
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация объекта"
        return context



'''Блок получения информации о объектах'''
@method_decorator(login_required, name='dispatch')
class DetailWorker(DetailView):
    """Информация о сотруднике"""

    model = Worker
    field = ('roles', 'name')
    template_name = "Management_app/card_worker.html"
    pk_url_kwarg = 'worker_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о сотруднике"
        return context

@method_decorator(login_required, name='dispatch')
class DatailBrigade(UpdateView, FormView):
    """Информация о бригаде и обновления"""

    model = Brigade
    template_name = "Management_app/card_brigade.html"
    form_class = UserBrigade
    pk_url_kwarg = 'brigade_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о бригаде"
        context['workers'] = context.get('object').workers.filter(roles='Механик')
        context['object'] = Objectes.objects.filter(brigades_id=context.get('object').pk)
        return context


''' '''
@method_decorator(login_required, name='dispatch')
class DataiObjects(DetailView, UpdateView):
    """Информацмя о объекте"""

    model = Objectes
    template_name = "Management_app/card_objectes.html"
    fields = ('status_work',)
    pk_url_kwarg = 'objectes_id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о объекте"
        return context

