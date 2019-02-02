from django.shortcuts import render
from .models import Resource

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def techtypes (request):
    type_list=Resource.objects.all()
    return render (request, 'club/types.html', {'type_list': type_list})

