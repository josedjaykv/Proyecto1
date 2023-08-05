#Los objetos HttpRequest y HttpResponse estan definidos en el modulo django.http
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render



class persona(object):
    
    #constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



#La fucion recibe un request, cada funcion en el archivo views son vistas
def saludo(request): #primera vista    
    p1 = persona('Jose', 'Vanegas')
    fecha_actual = datetime.datetime.now()
    temas_del_curso = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
 
    diccionario = {'nombre_persona':p1.nombre, 'apellido_persona':p1.apellido, 'fecha':fecha_actual, 'temas':temas_del_curso}
    return HttpResponse(render(request, "miplantilla.html", diccionario))



def despedida(request):
    return HttpResponse("Chao gente, vamos a ganar todas las materias del semestre con la ayuda de Dios")



def fecha(request):    
    #funcion de la clase datetime que da la fecha actual
    fecha_actual = datetime.datetime.now()

    mensaje = """<html>
    <body>
    <h2>
    Fecha y hora actual %s
    </h2>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(mensaje)



#Pasar parametros
def calEdad(request, year, edad):

    periodo = year - 2023
    edadFutura = edad+periodo
    
    mensaje = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(year, edadFutura)

    return HttpResponse(mensaje)
    #http://localhost:8000/edades/2050

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "CursoC.html", {"fecha":fecha_actual})

def cursoCss(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "CursoCss.html", {"fecha":fecha_actual})

