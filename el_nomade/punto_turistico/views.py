

# Create your views here.
from django.shortcuts import render, redirect
from .models import PuntoTuristico
from .forms import PuntoTuristicoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

def create_punto_turistico(request):
    if request.method == 'POST':
        form = PuntoTuristicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_puntos_turisticos')
    else:
        form = PuntoTuristicoForm()
    return render(request, 'turismo/create.html', {'form': form})

def list_puntos_turisticos(request):
    puntos_turisticos = PuntoTuristico.objects.all()
    return render(request, 'turismo/list.html', {'puntos_turisticos': puntos_turisticos})

def update_punto_turistico(request, pk):
    punto_turistico = PuntoTuristico.objects.get(pk=pk)
    if request.method == 'POST':
        form = PuntoTuristicoForm(request.POST, request.FILES, instance=punto_turistico)
        if form.is_valid():
            form.save()
            return redirect('list_puntos_turisticos')
    else:
        form = PuntoTuristicoForm(instance=punto_turistico)
    return render(request, 'turismo/update.html', {'form': form})

def delete_punto_turistico(request, pk):
    punto_turistico = PuntoTuristico.objects.get(pk=pk)
    if request.method == 'POST':
        punto_turistico.delete()
        return redirect('list_puntos_turisticos')
    return render(request, 'turismo/delete.html', {'punto_turistico': punto_turistico})

# Vista para subir una imagen
@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        file_name = default_storage.save(image.name, image)
        file_url = default_storage.url(file_name)
        return JsonResponse({'url': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)