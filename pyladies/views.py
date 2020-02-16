from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from pyladies.models import EventInstance


# Create your views here.
def home_page(request):
    events = EventInstance.objects.filter(event_date__lte=timezone.now()).order_by('event_date')
    return render(request, 'home.html', {'events':events})
