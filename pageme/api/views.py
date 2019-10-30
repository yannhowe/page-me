from django.shortcuts import render
from django.http import HttpResponse

import subprocess

def helloworld(request):
    return HttpResponse("Hello, world. You're at the api index.")

def netpage(request):
    subprocess.call(["./cli/linux_64bit/netpage", "91235678", "-TSMS", "-g127.0.0.1"])
    return HttpResponse("Hello, world. You're at the netpage.")