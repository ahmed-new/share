
from django.urls import path 
from .views import Registeruserview ,Updateuserview ,PasswordsChangeView ,Showprofileview , Editprofilepageview , Creatprofilepageview

from . import views




urlpatterns = [

    path('register/',Registeruserview.as_view(),name='register'),
    path('edit_profile/',Updateuserview.as_view(),name='edit_profile'),
    path ('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('changed/', views.yes_changed , name = 'password-changed'),
    path('profile/<int:pk>',Showprofileview.as_view(),name='show_profile'),
    path('profile/edit/<int:pk>',Editprofilepageview.as_view(),name='edit_profile_page'),
    path('create_profile',Creatprofilepageview.as_view(), name='create_profile')


] 