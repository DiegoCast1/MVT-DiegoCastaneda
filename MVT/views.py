from contextvars import Context
from pipes import Template
from django.forms import DateTimeField
from django.http import HttpResponse
from django.shortcuts import render
from MVT.models import Familiar1 , Familiar2 , Familiar3
from django.template import loader
from datetime import date, datetime
from django.template import Template , Context

def familiar1(self):

    nombre = 'Camila'
    apellido = 'Castañeda'
    fecha = date(1994,2,15)
    anio = 28


    miHtml = open("D:/trabajos/MVT-DiegoCastaneda/MVT-DiegoCastaneda/MVTEntregable/plantilla/plantilla1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    miHtml.close() #Cerramos el archivo

    miContexto = Context({'nombre':nombre, 'apellido': apellido,'anio': anio , 'fecha': fecha }) 
                            
                            
                            #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    #plantilla = loader.get_template('plantilla1.html')
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)



def familiar2(self):

    nombre = 'Marianela'
    apellido = 'Angulo'
    fecha = date(1957,6,7)
    anio = 66


    miHtml = open("D:/trabajos/MVT-DiegoCastaneda/MVT-DiegoCastaneda/MVTEntregable/plantilla/plantilla2.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    miHtml.close() #Cerramos el archivo

    miContexto = Context({'nombre':nombre, 'apellido': apellido,'anio': anio , 'fecha': fecha }) 
                            
                            
                            #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    #plantilla = loader.get_template('plantilla1.html')
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)



def familiar3(self):

    nombre = 'Diego'
    apellido = 'Castañeda'
    fecha = date(1999,4,16)
    anio = 23


    miHtml = open("D:/trabajos/MVT-DiegoCastaneda/MVT-DiegoCastaneda/MVTEntregable/plantilla/plantilla3.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    miHtml.close() #Cerramos el archivo

    miContexto = Context({'nombre':nombre, 'apellido': apellido,'anio': anio , 'fecha': fecha }) 
                            
                            
                            #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    #plantilla = loader.get_template('plantilla1.html')
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)