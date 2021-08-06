from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import feedbackmodel,userRequest,Book,workerRequest
from django.forms import ModelForm
from django import forms



class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    class Meta:
        model=User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),

        }
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'input'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'input'}))


class FeedbackForm(ModelForm):
    Feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 8,'class':'input'}))
    class Meta:
        model=feedbackmodel
        fields=['username','Feedback']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
        }

class UserRequestForm(ModelForm):
    choices= [
        ("carpenter", "carpenter"),
        ("plumber", "plumber"),
        ("mechanic", "mechanic"),
        ("construction", "construction"),
        ("mining", "mining"),
        ("cook", "cook"),
        ("teacher", "teacher"),
    ]
    Work_type = forms.ChoiceField(choices=choices, required=True,widget=forms.Select(attrs={'class': 'input'}) )
    Description= forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'input'}))
    class Meta:
        model=userRequest
        fields="__all__"
        widgets = {

            'user': forms.TextInput(attrs={'class': 'input'}),
            'start_date': forms.TextInput(attrs={'class': 'input'}),
            'end_date': forms.TextInput(attrs={'class': 'input'}),
            'Place': forms.TextInput(attrs={'class': 'input'}),


        }




class workerRequestForm(ModelForm):

    class Meta:
        model=workerRequest
        fields=[ 'Clint','Name', 'Mobile','description']
        widgets = {

            'Name': forms.TextInput(attrs={'class': 'input'}),
            'Mobile': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'input'})
 }
class BookForm(ModelForm):

    class Meta:
        model=Book
        fields=['Username','worker_name']
        widgets = {

            'Username': forms.TextInput(attrs={'class': 'input'}),

        }


