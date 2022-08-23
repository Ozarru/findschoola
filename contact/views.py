from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm

# Create your views here.


def contact(req):
    form = ContactForm()
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            # auth_user = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                f'{subject}',
                f'{message}',
                f'{email}',
                # f'{auth_user}',
                ['joeyanyim@gmail.com'],
                fail_silently=False,
            )
            return redirect('home')
    context = {
        "contact_page": "active",
        "form": form,
        "title": 'contact', }
    return render(req, 'contact/index.html', context)
