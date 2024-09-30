from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from theblog.models import Profile
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from . forms import Signupform ,Updateprofileform , Passwordchangingform , Creatprofileform

class Registeruserview (generic.CreateView):
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    form_class= Signupform


class Loginuserview (generic.CreateView):
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    form_class= UserCreationForm

class Updateuserview (generic.UpdateView):
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')
    form_class= Updateprofileform

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    #form_class= PasswordChangeForm
    form_class= Passwordchangingform
    success_url=reverse_lazy('password-changed')


def yes_changed (request):
    return render (request ,'registration/password-changed.html',{})


class Showprofileview(generic.DetailView):
    model = Profile
    template_name = "registration/profile_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Showprofileview, self).get_context_data(*args, **kwargs)
        user_page = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['user_page'] = user_page
        return context


class Editprofilepageview(generic.UpdateView):
    model= Profile
    template_name="registration/edit_profile_page.html"
    fields=['bio','profile_pic','website','facebook','twitter','instagram']
    success_url=reverse_lazy('home')

class Creatprofilepageview(generic.CreateView):
    model=Profile
    template_name='registration/creat_profile_page.html'
    form_class = Creatprofileform

    def form_valid(self, form) :
        form.instance.user = self.request.user
        return super().form_valid(form)