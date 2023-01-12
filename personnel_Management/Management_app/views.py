from django.shortcuts import render

from Management_app.forms import User_brigade


def home(request):
    form = User_brigade
    context = {
        "form": form
    }
    return render(request, "Management_app/content.html", context=context)

