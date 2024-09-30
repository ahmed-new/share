from django.contrib.auth.forms import UserCreationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

class Signupform (UserCreationForm):
    Email_address= forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    phone_number=forms.CharField(max_length=20)
    class Meta():
        model = User
        fields=('username','first_name','last_name','password1','password2','phone_number')



class Updateprofileform (UserChangeForm):
    Email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta():
        model = User
        fields=('username','first_name','last_name','Email_address','password', 'phone_number',)


class Passwordchangingform (PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password1=forms.CharField(max_length=100 ,widget=forms.PasswordInput(attrs={'class': 'form-control', "type":"password"}))
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', "type":"password"}))
        
    class Meta():
        model = User
        fields=('old_password','new_password1','new_password2',)

 
class Creatprofileform(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['bio','profile_pic','website','facebook','twitter','instagram']

        widgets={

            'bio':forms.Textarea(attrs={'class':'form_control'}),
            #'profile_pic':forms.Textarea(attrs={'class':'form_control'}),
            'website':forms.TextInput(attrs={'class':'form_control'}),
            'facebook':forms.TextInput(attrs={'class':'form_control'}),
            'twitter':forms.TextInput(attrs={'class':'form_control'}),
            'instagram':forms.TextInput(attrs={'class':'form_control'}),

        }