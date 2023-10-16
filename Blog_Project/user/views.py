from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    context = {
        'form' : form,
    }
    return render(request, 'user/sign_up.html', context)

def profile(request):
    return render(request, 'user/profile.html')