from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import user_form , user_updateform , profile_updateform
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form=user_form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username} , log in now!')
            return redirect('login')
    else:
        form=user_form()
    return render(request,'users/register.html',{'form':form , 'title':"Register"})
@login_required
def profile(request):
    if request.method=='POST':
        u_form=user_updateform(request.POST,instance=request.user)
        p_form=profile_updateform(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account Updated!')
            return redirect('profile')
    else:
        u_form=user_updateform(instance=request.user)
        p_form=profile_updateform(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
        'title':'Profile'
    }
    return render(request,'users/profile.html',context)
class user_page(DetailView):
    model = User
    template_name='users/user_page.html'
    context_object_name='user'
