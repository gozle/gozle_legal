from django.urls import path 
from . import views

app_name = "documents"

urlpatterns = [
    path("<int:id>", views.view_document, name = "viewDocument"),
    path("form/", views.add_document_view, name = "addDocument"),
    path("edit/<int:id>", views.edit_document_view, name = "editView"),
    path("pdf/<int:id>", views.generate_pdf, name = "pdf")
]