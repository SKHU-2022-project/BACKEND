from django.urls import path
from media import views

urlpatterns = [
	path('mediacontent/test/', views.mediacontentTest, name='mediacontentTest'),
    path('mediacontent/submit/', views.mediacontentSubmit, name='mediacontentSubmit'),
    path('mediacontent/result/<int:major_id>/', views.mediacontentResult, name='mediacontentResult'),
    
    path('mediacontent/engtest/', views.mediacontentEngTest, name='mediacontentEngTest'),
    path('mediacontent/engsubmit/', views.mediacontentEngSubmit, name='mediacontentEngSubmit'),
    path('mediacontent/engresult/<int:major_id>/', views.mediacontentEngResult, name='mediacontentEngResult'),
    
    path('mediacontent/chtest/', views.mediacontentCnTest, name='mediacontentCnTest'),
    path('mediacontent/chsubmit/', views.mediacontentCnSubmit, name='mediacontentCnSubmit'),
    path('mediacontent/chresult/<int:major_id>/', views.mediacontentCnResult, name='mediacontentCnResult'),
    
    path('mediacontent/board/', views.mediacontentBoard, name='mediacontentBoard'),
]