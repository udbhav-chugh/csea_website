from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.

def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        messages.success(
            request, 'Your account has been created! You can now login!')
        return redirect('/cseweb/csea/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def alumni(request):
    if request.user.is_authenticated==0:
        return redirect('/cseweb/csea/login/')
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
        messages.success(request, 'Profile updated')
        return redirect('/cseweb/csea/alumni/')
    u_form = UserUpdateForm(instance=request.user)
    context = {'u_form': u_form}
    return render(request, 'alumni.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/cseweb/csea/login/')
