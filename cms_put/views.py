from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

def pickPage(request, pageID):
    try:
        pagina = Pages.objects.get(id=pageID)
        respuesta = 'La pagina "' + pagina.name + '" dice: '\
                    + pagina.page
    except:
        respuesta = 'No se encontro esa pagina'
    return HttpResponse(respuesta)

@csrf_exempt
def newPage(request):
    print (request.body)    # Debug
    if request.method == 'GET':
        libro = Pages.objects.all()
        respuesta='<ol>'
        for pagina in libro:
            respuesta += '<li><a href="' + str(pagina.id) + '">'\
                        + pagina.name + '</a>'
        respuesta += '</ol>'
    elif request.method == 'PUT':
        try:
            info = request.body
            p = Pages(name=info.split(':')[0],\
                      page=info.split(':')[1])
            p.save()
            respuesta = 'Todo Ok!'
        except:
            respuesta = 'Nada Ok... El formato debe ser...Titulo: texto'

    return HttpResponse(respuesta)
