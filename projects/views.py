from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our Products')

def project(request,pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))
