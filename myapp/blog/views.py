from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def index(request):
    return HttpResponse("Hello I am rukaa")

def detail(request,post_id):
    return HttpResponse(f'Hello I am rukaa .And the id is {post_id}')

def old_url_view(request):
    return redirect(reverse('blog:new_url_page'))

def new_url_view(request):
    return HttpResponse("Hello I am rukaa")



