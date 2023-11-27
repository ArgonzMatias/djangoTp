
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from listado_incidentes.models import Incidente, Comunidad
@api_view(['GET'])
def article_detail(request, slug):
    comunidad = get_object_or_404(Comunidad, nombre=slug)
    incidentes = Incidente.objects.filter(miembro__comunidad=comunidad)
    return render(request, 'incident_list.html', {'incidentes': incidentes})

