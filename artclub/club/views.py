from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render



def index(request):
    return render(request, 'club/index.html')


def about(request):
    return render(request, 'club/about.html')


def events(request):
    return render(request, 'club/events.html')


def gallery(request):
    return render(request, 'club/gallery.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        form.save()

        try:
            send_mail(subject,name + ' ' + message + ' ' + from_email, from_email, ['arifulrian@gmail.com'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Thank you for your message.')
    context = {
            "form": form,
        }
    return render(request, 'club/contact.html', context)





def team(request):
    return render(request, 'club/team.html')
