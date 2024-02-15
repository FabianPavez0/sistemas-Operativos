from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Socio
import json

# Create your views here.


@csrf_exempt
def crear_socio(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        dni = body.get('DNI')
        numero_socio = body.get('numero_socio')
        contraseña = body.get('contraseña')
        if dni and numero_socio and contraseña:
            nuevo_socio = Socio(dni=dni, numero_socio=numero_socio, contraseña=contraseña)
            nuevo_socio.save()
            return JsonResponse({"Info": "Socio creado correctamente"})
        else:
            return JsonResponse({}, status=400)
    else:
        return JsonResponse({}, status=405)

@csrf_exempt
def modificar_contraseña(request, dni):
    if request.method == 'POST':
        try:
            socio = Socio.objects.get(dni=dni)
        except Socio.DoesNotExist:
            return JsonResponse({}, status=404)
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        nueva_contraseña = body.get('contraseña')
        if nueva_contraseña:
            socio.contraseña = nueva_contraseña
            socio.save()
            return JsonResponse({"Info": "Contraseña modificada correctamente"})
        else:
            return JsonResponse({}, status=400)
    else:
        return JsonResponse({}, status=405)


@csrf_exempt
def obtener_todos_socios(request):
    if request.method == 'GET':
        socios = Socio.objects.all().values()
        return JsonResponse(list(socios), safe=False)
    else:
        return JsonResponse({}, status=405)


