from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label =''
        self.fields['username'].help_text = '<span class="form-text text-muted">Your Name</span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Your Password</span>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
<<<<<<< HEAD
        self.fields['password2'].lablel = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Your Password Must match</span>'
=======
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Your Password Must match</span>'
>>>>>>> 871174d ('correct_spellin')
