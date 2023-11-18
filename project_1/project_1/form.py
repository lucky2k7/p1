from django import forms 
 
class UserForm(forms.Form):
    name = forms.CharField(label="name", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.CharField(label="email", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

class subjects(forms.Form):
    subject1 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject3 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject4 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject5 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject6 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))