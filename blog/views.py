from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import post
from django.views.generic import (ListView ,
 DetailView, 
 CreateView,
 UpdateView ,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    data={
        'post':post.objects.all(),
        'title':'Home'
    }
    
    return render(request,'blog/home.html',data)
class postlistview(ListView):
    model=post
    template_name='blog/home.html'
    context_object_name='post'
    ordering=['-date_posted']
    paginate_by = 5
class user_postlistview(ListView):
    model=post
    template_name='blog/user_posts.html'
    context_object_name='post'
    paginate_by = 5
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')



class postdetailview(DetailView):
    model=post
    context_object_name='x' # default name is "object"
class CreatePost(LoginRequiredMixin ,CreateView):
    model=post
    fields=['title','contenet']
    template_name='blog/create_post.html' # default name'/post_form.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class UpdatePost(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model=post
    fields=['title','contenet']
    template_name='blog/create_post.html' # default name'/post_form.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        return post.author==self.request.user
class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url='/'
    #context_object_name='x' # default name is "object"
    def test_func(self):
        post=self.get_object()
        return post.author==self.request.user
    
    

def about(request):
   
    return render(request,'blog/about.html',{'title':'About'})