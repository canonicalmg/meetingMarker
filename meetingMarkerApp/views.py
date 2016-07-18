from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Meeting
# Create your views here.

def index(request):
    #return HttpResponse("Arrived.")
    template = loader.get_template('meetingMarkerApp/index.html')
    meetings = Meeting.objects.filter()
    context = {
        "meetings": meetings
    }
    return HttpResponse(template.render(context, request))