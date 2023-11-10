from django import forms 
 
class UserForm(forms.Form):
    name = forms.CharField(label="name", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.CharField(label="email", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))