from django.shortcuts import render, redirect
from .forms import Form
from django.contrib import messages

# def accounts(request):
#     return render(request, 'accounts/accounts.html')



def signup_view(request):
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration was successful!")
            return redirect('login') 
        else:
            messages.error(request, "Please enter the information correctly.")

    else:
        form = Form()

    return render(request, 'accounts/signup.html', {'form': form})

