# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'attempt_number' not in request.session:
        request.session['attempt_number'] = 0
    return render(request, 'my_app/index.html')
def attempt(request):
    request.session['attempt_number'] += 1
    request.session['generate'] = get_random_string(length=14)
    return redirect('/')
def reset(request):
    del request.session['attempt_number']
    return redirect('/')