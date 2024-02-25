from django.shortcuts import render
from django.core.cache import cache
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from .models import Category, Document, Language
from .forms import PostForm
from django_elasticsearch_dsl import search
from elasticsearch import Elasticsearch

CACHE_TTL = getattr(settings, "CACHE_TTL")

def add_document_view(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        context = {"allCategories":categories, "form":PostForm, "languages":Language.objects.all()}
        return render(request, "documents/add-document.html", context)
    return JsonResponse({"status":"500 Auth Error"})


        

def view_document(request, id):
    cached_categories = cache.get("cached_categories")
    cached_document = cache.get(f"cached_document{id}")
   

    if cached_categories is None or cached_document is None:
        categories = Category.objects.all()
        document = Document.objects.get(id = id)

        cache.set(f'cached_document{id}', document, CACHE_TTL)
        cache.set('cached_categories', categories, CACHE_TTL)
    else:
        categories = cached_categories
        document = cached_document

    context = {"document" :document, "allCategories":categories}
    return render(request, "core/view-document.html", context)


def edit_document_view(request, id):
    if request.user.is_authenticated:
        document = Document.objects.get(id = id)
        form = PostForm({"body":document.body})
        context = {"document":document, "form":form, 
                   "allCategories":Category.objects.all(),
                   "languages":Language.objects.all()}
        return render(request, "documents/edit-document.html", context)




