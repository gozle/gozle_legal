from django.shortcuts import render
from django.core.cache import cache
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from .models import Category, Document
from .forms import PostForm
from .utils import get_language_choices

CACHE_TTL = getattr(settings, "CACHE_TTL")

def add_document_view(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        languages = get_language_choices()
        context = {"allCategories":categories, "form":PostForm, "languages":languages}
        return render(request, "documents/add-document.html", context)
    return JsonResponse({"status":"500 Auth Error"})

def add_document(request):
    form = PostForm(request.POST)
    if request.method == "POST" and form.is_valid() and request.user.is_authenticated:
        body = form.cleaned_data['body']
        header = request.POST["header"]
        category_id = request.POST["category"]
        category = Category.objects.get(id = category_id)
        f = Document(header = header,body = body, category = category)
        f.save()
        return HttpResponseRedirect(reverse("core:category", kwargs={"id":category_id}))
        

def view_document(request, id):
    cached_categories = cache.get("cached_categories")
    cached_document = cache.get("cached_document")

    if cached_categories is None or cached_document is None:

        categories = Category.objects.all()
        document = Document.objects.get(id = id)

        cache.set('cached_document', document, CACHE_TTL)
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
        context = {"document":document, "form":form, "allCategories":Category.objects.all()}
        return render(request, "documents/edit-document.html", context)

def edit_document(request,id):
    document = Document.objects.get(id = id)
    form = PostForm(request.POST)
    if request.method == "POST" and form.is_valid() and request.user.is_authenticated:
        body = form.cleaned_data['body']
        category_id = request.POST["category"]
        category = Category.objects.get(id = category_id)
        document.body = body
        document.category = category
        document.save()
        return HttpResponseRedirect(reverse("documents:viewDocument", kwargs= {"id":id}))
    return JsonResponse({"status":"500 Auth Error"})

def delete_documet(request,id):
    if request.method =="POST" and request.user.is_authenticated:
        document = Document.objects.get(id = id)
        document.delete()
        return JsonResponse({"status": "Successfully deleted!"})
    return JsonResponse({"status":"500 Auth Error"})


