from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):

    list_articles=Article.objects.all()
    context={"Listes_articles":list_articles}
    return render(request,'index.html',context)