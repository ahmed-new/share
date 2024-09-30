
from django.urls import path 
from .views import home ,viewdetail , Addpostview , Updatepostview ,deletepostview , Addcategoryview ,ctigoriesview ,likesview ,Addcommenttview


urlpatterns = [
   path('',home.as_view(), name='home'),
   path('artical/<int:pk>',viewdetail.as_view(), name='artical_detail'),
   path('add_post/',Addpostview.as_view(), name='add post'),
   path('add_category/',Addcategoryview.as_view(), name='add category'),
   path('artical/edit/<int:pk>',Updatepostview.as_view(),name='update_post'),
   path('artical/<int:pk>/remove',deletepostview.as_view(),name='delete_post'),
   path('ctigories/<str:cats>',ctigoriesview,name='ctigories'),
   path('likes/<int:pk>',likesview , name='like_post'),
   path('artical/<int:pk>/comment',Addcommenttview.as_view(), name='add comment'),
] 