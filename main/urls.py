from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', include('it.urls')),
    path('', include('humanity.urls')),
    path('', include('society.urls')),
    path('', include('media.urls')),
    path('it/board/', views.itboard, name='itBoard'),
    path('mediacontent/board/', views.mediacontentBoard, name='mediacontentBoard'),
    path('society/board/', views.societyBoard, name='societyBoard'),
    path('humanity/board/', views.humanityBoard, name='humanityBoard'),
]