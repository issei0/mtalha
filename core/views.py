from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    context = {
       'images': Image.objects.all(),
    }
    return render(request, "index.html", context)