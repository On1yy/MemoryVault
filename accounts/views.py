from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('/')


    else:
        form = RegisterForm()

    return render(request,'accounts/register_form.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect('/memory/list')

    else:
        form = LoginForm()

    return render(request, 'accounts/login_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
