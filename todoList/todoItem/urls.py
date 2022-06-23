from django.urls import path
from . import views

urlpatterns = [
    path('folders/', views.Folders.as_view()),
    path('folders/<str:pk>/', views.FoldersRUD.as_view()),
]