from django.shortcuts import render
from rest_framework import viewsets
from .serilizers import MovieSerializer
from .models import Moviedata
from django.core.paginator import Paginator



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


def movie_list(request):
    movies = Moviedata.objects.all()
    paginator = Paginator(movies, 10)  # Show 10 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movies/movie_list.html', {'page_obj': page_obj})