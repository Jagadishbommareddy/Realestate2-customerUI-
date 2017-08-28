from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm



def hello(request):
    return HttpResponse("hello, world")


def helloparams(request, param):
    return HttpResponse("param value: {0}".format(param))


def index(request):
    return render(request, "index.html")


def people(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            p = CustomerForm()
            p.first_name = form.cleaned_data["first_name"]
            p.last_name = form.cleaned_data["last_name"]
            p.age = form.cleaned_data["age"]
            p.save()
        else:
            form = CustomerForm()

    po = Customer.objects.all()
    return render(request, "people.html", {"people": po, "form": form})
