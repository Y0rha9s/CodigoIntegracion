from django.shortcuts import render
import requests

def cart(request):

    control = { 'image' : 'img/HerramientasManuales/alicate.webp',
                'product': 'Alicate cortante stanley',
                'description': '',
                'price' : 9900,
                'quantity': 1
                }
    gabinete = {'image' : 'img/HerramientasManuales/esmerilBau.webp',
                'product': 'Esmeril Baucker',
                'description': '',    
                'price' : 33790,
                'quantity': 1
                }
    notebook = {'image' : 'img/HerramientasManuales/martilloStanley.webp',
                'product': 'MAtillo Stanley',
                'description': '',    
                'price' : 20990,
                'quantity': 1
                }

    products = [control, gabinete, notebook]
    total = control.get('price') + gabinete.get('price') + notebook.get('price')

    return render(request, 'home2.html', {'products' : products, 'total': total})  