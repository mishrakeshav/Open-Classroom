from django.shortcuts import render
from newsletter.forms import SubscribeForm
from contactus.forms import ContactUsForm

def landing(request):
    subscribe_form = SubscribeForm()
    contactus_form = ContactUsForm()
    context = {
        'title': "Home",
        'subscribe_form':subscribe_form,
        'contactus_form':contactus_form
        }
    return render(request, "landing_page.html", context)
