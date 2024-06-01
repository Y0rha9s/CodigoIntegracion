from django.shortcuts import render, redirect
import traceback
from django.contrib.auth import login as login_user, authenticate, logout as logout_user
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def login(request):
    
    if request.method== 'GET':
        return render(request, 'login.html',{'message:error' : None})
    elif request.method== 'POST':
        try:
            print('request_post:', request.POST)
            user = request.POST['username']
            password = request.POST['password']
            
            username = authenticate(username=user, password=password)
            print('username: ', username)
            if username is not None:
                    login_user(request, username)
                    return redirect('/home/')
            else:
                return render(request, 'login.html', {'message_error' : 'Usuario o Contraseña invalida'})
        except Exception as e:
            traceback.print_exc()
            return render(request, 'login.html', {'message_error' : 'Error inesperado intente mas tarde'})

def logout(request):
    print('logout')
    try:
        logout_user(request)
    except Exception as e:
        print('Error: ', e)
    return redirect('/home/')

def update_pass(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        secret = request.POST.get('password')
        secret2 = request.POST.get('password2')
        print('username', username)
        print('secret: ',secret)
        print('secret2: ',secret2)
        
        if secret != secret2 :
            context = {'message_error': 'Contraseñas no coinciden'}
            print('context: ',context)
            return render(request,'update-secret.html', context)
        
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist as e:
            user = None
        print('user: ', user)
        
        if user is not None:
            user.set_password(secret)
            user.save()
            context = {'message:': 'Contraseña actualizada'}
        else:
            context = {'message_error:':'Problemas al actuializar la contraseña.'}
        print('context: ', context)
        return render(request,'update-secret.html', context)
    elif request.method == 'GET':
        context = {}
        return render(request,'update-secret.html', context)
