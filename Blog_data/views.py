# Django
from django.conf.urls import handler404, handler500
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
# Rest
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, serializers, viewsets
from rest_framework.response import Response
from rest_framework import permissions
from Blog_data.serializers import PostSerializer, TableSerializer
# Model
from .models import Post, Table
from django.conf import settings
import json

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TableDataViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class RegisterListCreate(generics.ListCreateAPIView):
    model = Post
    queryset = model.objects.all()
    serializers_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def about(request):
    return render(request, 'about.html')


def ouath(request):
    return render(request, 'OuathPage.html')


def login(request):
    return render(request, './User/login.html')


def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response


def test(request):
    print('Work')
    if request.method == 'GET':
        return JsonResponse({'Message':'GET'})
    elif request.method == 'POST':
        print("看一下結果: ", request.body)
        data = json.loads(request.body.decode("utf-8"))
        return JsonResponse({'Message':'POST', 'Message':data})

def BootStrip(request):
    return render(request, './BootStrap/BootStrap.html')

def iframe(request):
    return render(request, 'test.html')