from django import forms
from .models import Post ,Category , Comment


choices=Category.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
    choices_list.append(item)

class Addpostform(forms.ModelForm):
    class Meta():
        model = Post
    
        
        fields=["title","author","category","body","header_img"]
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'author':forms.TextInput(attrs={'class':'form-control' , 'value':'' ,'type':'hidden','id':"ahmed"}),
                 #'author':forms.Select(attrs={'class':'form-control'}),
                 'category':forms.Select(choices= choices_list , attrs={'class':'form-control'}),
                 'body':forms.Textarea(attrs={'class':'form-control'}),


        }

class Addcommentform(forms.ModelForm):
    class Meta():
        model = Comment
    
        
        fields=["body"]
        widgets={
            #'name':forms.TextInput(attrs={'class':'form-control'}),
                 'body':forms.Textarea(attrs={'class':'form-control'}),

        }
