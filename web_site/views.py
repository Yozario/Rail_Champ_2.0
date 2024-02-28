from django.shortcuts import render
from web_site.models import Railways


# Create your views here.
def index(request):
    a = Railways.objects.all()
    b = Railways.objects.all()
    return render(request, 'index.html', context={'data': a, 'r': b[0].id})

def rules(request):
    return render(request, 'rules.html')

def maps(request):
    return render(request, 'maps.html')