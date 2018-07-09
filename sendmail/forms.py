from django import forms

class ComposeMail(forms.Form):
	   reciever = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
	   subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	   msg = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))