from django.shortcuts import render
from django.http import request

# Create your views here.
def view_humanize(request):
    data = {
        "Value1" : 1200000,
        "Position": 1
    }

    return render(request, "django_templates\humanize.html", data)