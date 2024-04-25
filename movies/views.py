from django.shortcuts import render
from rest_framework import viewsets
from .serilizers import MovieSerializer
from .models import Moviedata


# Create your views here.
# View with adding option
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


# View without adding option
# class MovieViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Moviedata.objects.all()
#     serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerializer
