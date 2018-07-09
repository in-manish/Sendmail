from django.shortcuts import render
from sendmail.forms import ComposeMail

# Create your views here.

def composemail(request):
	if request.method == 'POST':
		xmail = ComposeMail(request.POST)
		# if xmail.is_valid():
		# reciever = xmail.cleaned_data['reciever']
		# subject = xmail.cleaned_data['subject']
		# msg = xmail.cleaned_data['msg']
		return render(request, 'sendmail/composemail.html',{'current_name':xmail} )
	return render(request, 'sendmail/composemail.html', {'current_name':ComposeMail(request.GET)})

def home(request):
	return render(request, 'sendmail/index.html', {})