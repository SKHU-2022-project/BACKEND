from django.urls import path
from society import views

urlpatterns = [
	path('society/test/', views.societyTest, name='societyTest'),
    path('society/submit/', views.societySubmit, name='societySubmit'),
    path('society/result/<int:major_id>/', views.societyResult, name='societyResult'),
    
    path('society/engtest/', views.societyEngTest, name='societyEngTest'),
    path('society/engsubmit/', views.societyEngSubmit, name='societyEngSubmit'),
    path('society/engresult/<int:major_id>/', views.societyEngResult, name='societyEngResult'),
    
    path('society/chtest/', views.societyCnTest, name='societyCnTest'),
    path('society/chsubmit/', views.societyCnSubmit, name='societyCnSubmit'),
    path('society/chresult/<int:major_id>/', views.societyCnResult, name='societyCnResult'),
    
    path('society/board/', views.societyBoard, name='societyBoard'),
]