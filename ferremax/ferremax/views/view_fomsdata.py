from django.shortcuts import render
from ferremax.models.models import Contact

def formsdata(request):
    return render(request, 'forms-data.html', {'active_formsdata': 'active'})

def guardar(request):
    print('request: ', request)
    print('request.method: ', request.method)
    if request.method == 'POST':
        print('INVOCADO POR POST')
        # LECTURA DE LOS PARAMETROS PROVENIENTES DEL FORMULARIO
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        telefono = request.POST['telefono']
        # CRAENDO UN OBJETO DE TIPO MODEL (CRUD)
        datos = Contact()
        # ASIGNANDO VALORES A LOS ATRIBUTOS DEL OBJETO
        # DE TIPO MODEL
        datos.nombres = nombres
        datos.apellidos = apellidos
        datos.telefono = int(telefono)
        message = None
        message_error = None
        try:
            datos.save()
            message = "Registro almacenado."
        except Exception as e:
            message_error = "Error intente más tarde."
        return render(request, 'forms-data-guardar.html', {'datos' : datos, 'message': message, 'message_error': message_error})        
    else:
        return render(request, 'error.html', {})
