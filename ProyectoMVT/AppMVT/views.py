import email
from django.shortcuts import render
from AppMVT.models import HIJO
from django.http import HttpResponse 
import datetime

from AppMVT.models import MAMA
from AppMVT.models import PAPA




def Hijo(self):
    Hijo= HIJO(nombre='Julian Roman',apellido='Perez',email='juliperez@gmail.com',fecha='1990-10-19')
    Hijo.save()
    documentoDeTexto=f"--->Nombre:{Hijo.nombre}---Apellido:{Hijo.apellido}---Email:{Hijo.email}--Fecha_Nacimiento:{Hijo.fecha}"
    return HttpResponse(documentoDeTexto) 


def Papa(self):
    Papa= PAPA(nombre="Juan Roman",apellido="Perez",email="juanroman@gmail.com",profesion="medico")
    Papa.save()
    documentoDeTexto=f"--->Nombre:{Papa.nombre}----Apellido:{Papa.apellido}---Email:{Papa.email}---Profesion:{Papa.profesion}"
    return HttpResponse(documentoDeTexto)

def Mama(self):
    Mama= MAMA(nombre="Perla Luciana",apellido="Corol",email="perlitacorol@gmail.com",profesion="Abogada")
    Mama.save()
    documentoDeTexto=f"--->Nombre:{Mama.nombre}---Apellido:{Mama.apellido}--Email:{Mama.email}---Profesión:{Mama.profesion}" 
    return HttpResponse(documentoDeTexto) 


    