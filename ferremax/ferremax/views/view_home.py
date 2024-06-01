from django.shortcuts import render, redirect

def home(request):
    if request.user != None and request.user.__str__() != 'AnonymousUser':
        return render(request, 'home.html')
    else:
        return redirect('/login/')