from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!")

def dia_de_hoy(request):
    dia = datetime.now()
    return HttpResponse(f"Hoy es el día: <br>{dia}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context

def probando_template(request):
    # Abrimos el archivo html
    mi_html = open('./biblioteca_PF/plantillas/index.html')
    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())
    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()
    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()
    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)