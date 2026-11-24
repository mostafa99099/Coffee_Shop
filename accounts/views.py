from django.shortcuts import render, redirect
from .forms import Form
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


# def accounts(request):
#     return render(request, 'accounts/accounts.html')



def signup_view(request):
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration was successful!")
            return redirect('Base_Home') 
        else:
            messages.error(request, "Please enter the information correctly.")

    else:
        form = Form()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        data = AuthenticationForm(request, data=request.POST)

        if data.is_valid():

            login(request, data.get_user())
            
            messages.success(request, "login was successful!")
            
            return redirect('Base_Home')

        else:
            messages.error(request, "Please enter the information correctly.")
            return render(request, 'accounts/login.html', {'form': data})
        
    else:
        form = AuthenticationForm(request)

        return render(request, 'accounts/login.html', {'form': form})



        