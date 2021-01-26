from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout as logout_user


@require_http_methods(["POST", "GET"])
def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            messages.success(request, "Uživatel " + username + " úspěšně přihlášen.")
        else:
            messages.error(request, "Špatně zadané údaje.")
        return redirect('index')


@require_http_methods(["POST"])
def logout(request):
    messages.success(request, 'Úspěšné odhlášení.')
    logout_user(request)
    return redirect('index')
