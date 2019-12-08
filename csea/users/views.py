from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        messages.success(request, f'Account created for {email}!')
        return redirect('home:index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
