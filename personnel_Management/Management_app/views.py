from django.shortcuts import render

from Management_app.forms import User_brigade, User_Employee
from Management_app.models import Employee, Brigade


def home(request):
    return render(request, "Management_app/home.html")

def FormEmployee(request):
    form = User_Employee
    context = {
        "form": form
    }
    if request.method == "POST":
        form = User_Employee(request.POST)
        if form.is_valid():
            name_employee = form.cleaned_data["name_employee"]
            roles_id = int(form.cleaned_data["id_role"])
            print(roles_id)
            employee = Employee.objects.create(roles_id=roles_id, name_employee=name_employee)
    return render(request, "Management_app/content.html", context=context)


def FormBrigade(request):
    form = User_brigade
    context = {
        "form": form
    }
    if request.method == "POST":
        form = User_brigade(request.POST)
        if form.is_valid():
            citi = form.cleaned_data["citi"]
            foreman = int(form.cleaned_data["foreman"])
            mechanic = int(form.cleaned_data["mechanic"])
            print(citi,foreman, mechanic)

            brigade = Brigade.objects.create(сiti=citi)





    return render(request, "Management_app/brigade.html", context=context)


"""
def controllerFormEmployee(request):
    if request.method == "POST":
        form = User_Employee(request.POST)
        print(form)
        if form.is_valid():
            name_employee = form.cleaned_data["name_employee"]
            id_role = form.cleaned_data["id_role"]
            print(id_role, name_employee)
"""
