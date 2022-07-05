from xml.dom.expatbuilder import DOCUMENT_NODE
from django.http import HttpResponse 
from ast import Str
from mimetypes import init
from tokenize import String
from xmlrpc.client import DateTime
import datetime
from django.template import Context,Template,loader


def probandoTemplate(self):
    nom1="Julian Roman"
    nom2="Juan Roman"
    nom3="Perla luciana"
    lista_de_notas=[4,5,6,7,8,9,2,3,1]
    promedio=sum(lista_de_notas)/len(lista_de_notas)
    

    diccionario={'nombre1':nom1,'nombre2':nom2,'nombre3':nom3,'lista':lista_de_notas,'promedio':promedio}
    

    plantilla=loader.get_template('Template.html')

    documento=plantilla.render(diccionario)

    return HttpResponse(documento)