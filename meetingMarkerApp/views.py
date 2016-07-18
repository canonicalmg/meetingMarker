from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
    #return HttpResponse("Arrived.")
    template = loader.get_template('meetingMarkerApp/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))