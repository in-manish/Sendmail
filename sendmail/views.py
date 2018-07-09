from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


from sendmail.forms import ComposeMail

# Create your views here.

def composemail(request):
	if request.method == 'POST':
		xmail = ComposeMail(request.POST)
		if xmail.is_valid():
			send_mail(
				xmail.cleaned_data['subject'],
				xmail.cleaned_data['msg'],
				settings.EMAIL_HOST_USER,
				[xmail.cleaned_data['reciever']]
				)
			xmail=""
			return render(request, 'sendmail/composemail.html',{'current_name':xmail} )
	return render(request, 'sendmail/composemail.html', {'current_name':ComposeMail(request.GET)})

def home(request):
	return render(request, 'sendmail/index.html', {})