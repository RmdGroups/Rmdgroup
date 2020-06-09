from django.shortcuts import render

from django.shortcuts import render
def index(request):
    return render(request,"Home.html")


def gallery(request):
    return render(request,"Galarey.html")


def address(request):
    return render(request,"Contact.html")


def technolages(request):
    return render(request,"Techonlages.html")


def softwere(request):
    return render(request,"Softwere.html")


def registration(request):
    return render(request,"Registration.html")