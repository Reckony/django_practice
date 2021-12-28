from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner")


def date(request):
    return HttpResponse(f"This page was served at {datetime.now()}")


def about(request):
    return HttpResponse(
        """
        Hi, \n
        I am Software Engineer who is eager to develop coding skills, now building this small app using Django ;) \n
        """
    )
