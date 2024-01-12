from django.shortcuts import render

from .models import Article


# Create your views here.
def index(request):
    context = {'articles_list': Article.objects.all()}
    return render(request, 'articles/index.html', context)
