from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import user

# Create your views here.
def home(request):
    template = loader.get_template("app.html")
    context = {}
    return HttpResponse(template.render(context, request))

def menu(request):
    template = loader.get_template("menu.html")
    context = {}
    return HttpResponse(template.render(context, request))

def product(request):
    template = loader.get_template("product.html")
    context = {}
    return HttpResponse(template.render(context, request))

def sacola(request):
    template = loader.get_template("bag.html")
    context = {}
    return HttpResponse(template.render(context, request))

def adress(request):
    template = loader.get_template("adress.html")
    context = {}
    return HttpResponse(template.render(context, request))

def checkout(request):
    template = loader.get_template("checkout.html")
    context = {}
    return HttpResponse(template.render(context, request))

# DB Pattern
def CadastraUsuario(request):
    if request.method == 'POST':
        template = loader.get_template("app.html")
        email = request.POST.get("email")
        password = request.POST.get("password")
        name = request.POST.get("name")
        print(email, password, name)
        newUser = user(email=email, password=password, name=name)
        newUser.save()
        context = {}
        return HttpResponse(template.render(context, request)) 
def LogaUsuario(request):
    if request.method == 'POST':
        template = loader.get_template("app.html")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            EmailVerify = user.objects.get(email=email)
            PassVerify = user.objects.get(password=password)
            if(EmailVerify and PassVerify):
                print("Acesso Autorizado")
        except Exception as e:
            print(e)
        context = {}
        return HttpResponse(template.render(context, request)) 