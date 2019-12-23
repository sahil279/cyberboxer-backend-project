from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Congratulations, Your account has been created,your username is {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()



    return render(request,'users/registers.html',{'form':form})
