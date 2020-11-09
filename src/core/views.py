from django.shortcuts import render

def landing(request):
    context = {'title': "Home"}
    return render(request, "landing_page.html", context)
