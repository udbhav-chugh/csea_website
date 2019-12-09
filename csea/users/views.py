from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        messages.success(request, f'Your account has been created! You can now login!')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def alumni(request):
    return render(request, 'alumni.html')
