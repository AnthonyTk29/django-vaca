import string
from tkinter import StringVar
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .form import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from .utils import get_plot
import pandas as pd
import json
# Create your views here.
def index (request):
    nom_due = str(request.user)
    vacas=Vacas.objects.filter(nombre_empleado=nom_due)
    return render(request,'index.html',{'Vacas': vacas})

def About(request):
    return render(request,'about.html')

def Registro_produ(request):
    if request.method == "POST":
        nom_vaca = request.POST.get("nombre", None)
        nom_due = str(request.user)
        fecha = request.POST.get("fech", None)
        hora = request.POST.get("select", None)
        comi = request.POST.get("raza", None)
        le = request.POST.get("peso", None)
        va=Vacas.objects.filter(nombre_empleado=nom_due,nombre_vaca=nom_vaca)
        for i in va:
            idva=i.id_vaca
        twz=Produccion.objects.create(fecha_produc=fecha, horario=str(hora), comida=str(comi), leche=str(le),id_vaca_id=int(idva))
        twz.save()
        pro=Produccion.objects.filter(id_vaca_id=int(idva))
        messages.success(request, f'Vaca {nom_vaca} registrada')
        return render(request,'registro_produ.html',{'produccion': pro})
    else:
        return render(request,'registro_produ.html')

def Registro_vacas(request):
    if request.method == "POST":
        nom_vaca = request.POST.get("nombre_vaca", None)
        nom_due = str(request.user)
        num = request.POST.get("num_vaca", None)
        color = request.POST.get("color", None)
        fecha = request.POST.get("fech", None)
        raza = request.POST.get("raza", None)
        peso = request.POST.get("peso", None)
        twz=Vacas.objects.create(nombre_empleado=nom_due, nombre_vaca=nom_vaca, num_vaca=num, color_vaca=color,fecha_nacimiento=fecha,raza_vaca=raza,Peso_vaca=peso)
        twz.save()
        messages.success(request, f'Vaca {nom_vaca} registrada')
    return render(request,'registro_vacas.html')

def Perfilvacas(request):
    return render(request,'perfilvacas.html')

def Totalleche(request):
    if request.method == "POST":
        nom_vaca = request.POST.get("fecha", None)
        print(nom_vaca)
    return render(request,'lechetotal.html')

def Datosvacas(request,a):
    nom_due = str(request.user)
    vacas=Vacas.objects.filter(nombre_empleado=nom_due,nombre_vaca=a)
    return render(request,'datosvacas.html',{'Vacas': vacas})

def Ingresarleche(request):
    l_lec=[]
    nom_due = str(request.user)
    va=Vacas.objects.filter(nombre_empleado=nom_due)
    for i in va:
        idva=i.id_vaca
        pro=Produccion.objects.filter(id_vaca_id=int(idva))
        for x in pro:
            le=x.leche
            l_lec.append(int(le))
    s=sum(l_lec)
    vac=len(va)
    list_pre={'suma' : s, 'contar' : vac}
    print(vac,s)
    return render(request,'ingleche.html',{'lista': list_pre})

def Prediccion(request):
    l_lec=[]
    l_k=[]
    nom_due = str(request.user)
    va=Vacas.objects.filter(nombre_empleado=nom_due)
    for i in va:
        idva=i.id_vaca
        pro=Produccion.objects.filter(id_vaca_id=int(idva))
        for x in pro:
            le=x.leche
            k=x.comida
            l_lec.append(int(le))
            l_k.append(int(k))
    #list_pre={ l_lec: l_k}
    li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    li1=[1, 2, 2, 4, 5, 4, 6, 7, 9, 10, 11, 12, 10, 14, 11]
    chart=get_plot(li,li1)
    return render(request,'prediccion.html',{'chart': chart})

def Registros(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = UserRegisterForm()
    context={ 'form' : form }
    return render(request,'registro.html',context)