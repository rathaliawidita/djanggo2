# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class IndexCoba(TemplateView):
    template_name="todos/index_todo.html"

def get(self, request, *args, **kwargs):
    print('get request method called ')
    return HttpResponse('hello get')

def index(request):
    return HttpResponse('rathalia widita')

def add(request,no1, no2):
    result = no1 + no2
    return HttpResponse('The result is : ' + str(result))

def cth_html(request):
    return render(request=request, template_name='todos/index_todo.html')

def contoh(nama):
    print(nama)





