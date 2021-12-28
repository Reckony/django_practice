from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count(),
                   "meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse(f"This page was served at {datetime.now()}")


def about(request):
    return HttpResponse(
        """
        Hi, \n
        I am Software Engineer who is eager to develop coding skills, now building this small app using Django ;) \n
        """
    )


