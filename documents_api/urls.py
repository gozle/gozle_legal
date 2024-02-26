from django.urls import path
from . import views

urlpatterns = [
    path("", views.DocumentApi.as_view()),
    path("<int:id>", views.DocumentDetailsApi.as_view())
]
