from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
@login_required()
def index(request):
    return render(request, "layout/dashboard-layout.html")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            group = None
            if user is not None:
                login(request, user)
                return redirect('core:index')


    else:
        form = AuthenticationForm()
    return render(request, 'login.html', context={'login_form': form})


def logout_request(request):
    logout(request)

    return redirect("core:login")
