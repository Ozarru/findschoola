from django.shortcuts import render

# Create your views here.


def contact(req):
    context = {
        "contact_page": "active",
        "title": 'contact', }
    return render(req, 'contact/index.html', context)
