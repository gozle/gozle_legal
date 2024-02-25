from django.shortcuts import render
from django.core.cache import cache
from django.conf import settings
from documents.models import Category, Document, Language

CACHE_TTL = getattr(settings, "CACHE_TTL")

def index(request):
    cached_documents = cache.get("cached_documents")
    cached_categories = cache.get("cached_categories")

    if cached_documents is None or cached_categories is None:
        try:
            all_categories = Category.objects.all()
            documents = Document.objects.all()

            cache.set('cached_documents', documents, CACHE_TTL)
            cache.set('cached_categories', all_categories, CACHE_TTL)
        except Exception as e:
            print("Error fetching data from the database:", e)
            # Handle the error appropriately, e.g., return an error response

    else:
        print("Data found in cache.")

        all_categories = cached_categories
        documents = cached_documents
    print(Language.objects.all())
    context = {"allCategories": all_categories, "documents": documents, "languages":Language.objects.all()}
    return render(request, "core/index.html", context)


def get_category(request, id):
    cached_category = cache.get("cached_category")
    cached_categories = cache.get("cached_categories")
    cached_documents = cache.get("cached_documents")

    if cached_documents is None or cached_categories is None or cached_category is None:

        all_categories = Category.objects.all()
        category = Category.objects.get(pk = id)
        documents = Document.objects.filter(category = category)
        
        cache.set("cached_category", category, CACHE_TTL)
        cache.set("cached_categories", all_categories, CACHE_TTL)
        cache.set("cached_documents", documents, CACHE_TTL)
    else:
        all_categories = cached_categories
        category = cached_category
        documents = cached_documents

    context = {"allCategories":all_categories,"category":category, "documents":documents}
    return render(request,"core/index.html", context)   

def select_language_document(request, id):
    language = Language.objects.get(id = id)
    documents =  Document.objects.filter(language = language)
    categories = Category.objects.filter(language = language)
    context = {"allCategories":categories,"documents":documents, "languages":Language.objects.all()}
    return render(request, "core/index.html", context)