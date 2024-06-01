from django.shortcuts import render
from ferremax.models.models import Region

def create(request):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    region = Region()
    region.nombre = nombre
    region.descripcion = descripcion
    region.save()
    regiones = Region.objects.all()
    data = {
            'active_region': 'active', 
            'message_state': '',
            'message': 'Región Creada',
            'regiones': regiones,
            }        
    return render (request, 'region.html', data)

def delete(request):
    id = request.POST['id']
    region = Region.objects.get(pk=id)
    nombre_region = region.nombre
    region.delete()
    regiones = Region.objects.all()
    data = {
            'active_region': 'active', 
            'message_state': '',
            'message': 'Región Eliminada id: {0} nombre: {1}'.format(id, nombre_region),
            'regiones': regiones,
            }        
    return render (request, 'region.html', data)    
    
def region(request):
    if request.method == 'GET':
        regiones = Region.objects.all()                
        data = {
                'active_region': 'active', 
                'message_state': 'd-none',
                'message': '',
                'regiones': regiones,                
                }
        return render (request, 'region.html', data)
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'CREATE':
            return create(request)
        if action == 'DELETE':
            return delete(request)