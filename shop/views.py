from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader


def LandingView(request):
    return render(request, 'shop/landingpage.html')


def LoginView(request):
    return render(request, 'shop/loginpage.html')
