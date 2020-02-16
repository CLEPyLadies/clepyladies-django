from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    return render(request, 'home.html')
