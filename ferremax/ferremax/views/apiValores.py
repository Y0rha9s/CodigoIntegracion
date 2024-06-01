import json
from datetime import datetime
from django.http import HttpResponse
from ferremax.views import indicadores

def procesar_json(request):
    # El JSON como cadena de texto
    json_data = {
        "version": "1.7.0",
        "autor": "mindicador.cl",
        "fecha": "2024-06-01T01:00:00.000Z",
        # ... (resto del JSON)
    }

    # Deserializar el JSON
    data = json.loads(json_data)

    # Iterar sobre los indicadores y guardar en la base de datos
    for indicador, valores in data.items():
        if indicador != "version" and indicador != "autor" and indicador != "fecha":
            indicador_obj = indicadores(
                codigo=valores["codigo"],
                nombre=valores["nombre"],
                unidad_medida=valores["unidad_medida"],
                fecha=datetime.strptime(valores["fecha"], "%Y-%m-%dT%H:%M:%S.%fZ"),
                valor=valores["valor"]
            )
            indicador_obj.save()

    return HttpResponse("Datos guardados correctamente")