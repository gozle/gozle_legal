from django.shortcuts import render
from django.core.cache import cache
from django.urls import reverse

from django.http import HttpResponseRedirect, JsonResponse, FileResponse
from django.conf import settings
from .models import Category, Document, Language
from .forms import PostForm

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.template.defaultfilters import striptags
from reportlab.lib.units import inch

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

def generate_pdf(request, id):
    document = Document.objects.get(id=id)

    header = striptags(document.header)  # Strip HTML tags from header
    body = striptags(document.body)  # Strip HTML tags from body

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter)

    # Set font and size for header
    p.setFont("Helvetica-Bold", 14)
    header_width = p.stringWidth(header)
    p.drawString((letter[0] - header_width) / 2, letter[1] - 0.75 * inch, header)

    # Set font and size for body
    p.setFont("Helvetica", 12)
    body_width = p.stringWidth(body)
    p.drawString((letter[0] - body_width) / 2, letter[1] / 2, body)

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=document.header + ".pdf")