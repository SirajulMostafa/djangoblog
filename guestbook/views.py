from django.shortcuts import render
from  django.http import HttpResponse
from .models import Comment


def abc(request):
    return render(request, 'guestbook/signPage.html')


def index(request):
    comments = Comment.objects.all()
    context = { 'comments' : comments }
    return render(request,'guestbook/index.html', context)
