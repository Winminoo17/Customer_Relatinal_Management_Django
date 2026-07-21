from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SingUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        mdoel = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].lablel =''
        self.fields['username'].help_text = '<span class="form-text text-muted">Your Name</span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].lablel = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Your Password</span>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].lablel = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Your Password Must match</span>'