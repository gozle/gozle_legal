from django.urls import path 
from . import views

app_name = "documents"

urlpatterns = [
    path("<int:id>", views.view_document, name = "viewDocument"),
    path("form/", views.add_document_view, name = "addDocument"),
    path("add/", views.add_document, name = "add"),
    path("edit/<int:id>", views.edit_document_view, name = "editView"),
    path("edit/<int:id>/submit", views.edit_document, name = "edit"),
    path("delete/<int:id>", views.delete_documet, name = "delete")
]