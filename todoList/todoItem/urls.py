from django.urls import path
from . import views

urlpatterns = [
    # folder
    path('folders/', views.Folders.as_view()),
    path('folders/<str:pk>/', views.FoldersRUD.as_view()),

    # tag
    path('tags/', views.Tags.as_view()),
    path('tags/<str:pk>/', views.TagsRUD.as_view()),

    # todo item
    path('todoItems/', views.TodoItems.as_view()),
    path('todoItems/<str:pk>/', views.TodoItemsRUD.as_view()),
]