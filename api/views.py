from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response


class Hello(generics.GenericAPIView):
    def get(self, reqeust, *args, **kwargs):
        return Response({'hello' : 'hello'})