from django.http import HttpResponse
from django.shortcuts import render
from .tasks import printer
import platform


def hello(request):
    printer.delay()
    return HttpResponse(f"operating_system: {platform.system()}")
