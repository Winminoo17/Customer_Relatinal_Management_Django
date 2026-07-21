from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

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
        self.fields['password2'].lablel = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Your Password Must match</span>'


class AddRecordForm(forms.ModelForm):
    # Changed TextInput to CharField
    first_name = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    
    # Changed EmailInput to EmailField
    email = forms.EmailField(label="", required=True, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    
    phone = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    address = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address'}))
    city = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    state = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    zipcode = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}))
    
    # Changed Textarea to CharField + Textarea widget
    description = forms.CharField(label="", required=True, max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a description...', 'rows': 4}))
    
    class Meta:
        model = Record
        exclude = ('user',)
