from django.shortcuts import redirect, render 
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 

from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "User has been registered")

            return redirect('home')

    context = {
        'form': form, 
    }

    return render(
        request, 
        'register.html', 
        context 
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            
            messages.success(request, 'Logado com sucesso!')
            
            return redirect('home')
        
        messages.error(request, 'Login inválido')

    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
   
    return redirect('login')