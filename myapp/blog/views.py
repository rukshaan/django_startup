from django.shortcuts import render,redirect,render
from django.http import HttpResponse
from django.urls import reverse
import logging
# Create your views here.
posts=[
        {'id':1,'title':'Post1','content':'Content of Post1'},
        {'id':2,'title':'Post2','content':'Content of Post2'},
        {'id':3,'title':'Post3','content':'Content of Post3'},
        {'id':4,'title':'Post4','content':'Content of Post4'},
]

def index(request):
    blog_title='Latest Posts'
    
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})

def detail(request,post_id):
    post=next((item for item in posts if item['id']==post_id),None)
    logger=logging.getLogger("Testing")
    logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post':post})

def old_url_view(request):
    return redirect(reverse('blog:new_url_page'))

def new_url_view(request):
    return HttpResponse("Hello I am rukaa")



