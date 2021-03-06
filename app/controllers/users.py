from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from app.decorators import login_required


@require_http_methods(["POST", "GET"])
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        username = request.POST['username']
        user = authenticate(request, username=username, password=request.POST['password'])
        if user is not None:
            login_user(request, user)
            messages.success(request, "Uživatel " + username + " úspěšně přihlášen.")
        else:
            messages.error(request, "Špatně zadané údaje.")
        return redirect('index')


@login_required
@require_http_methods(["POST"])
def logout(request):
    messages.success(request, 'Úspěšné odhlášení.')
    logout_user(request)
    return redirect('index')
