from django.urls import path
from humanity import views

urlpatterns = [
	path('humanity/test/', views.humanityTest, name='humanityTest'),
    path('humanity/submit/', views.humanitySubmit, name='humanitySubmit'),
    path('humanity/result/<int:major_id>/', views.humanityResult, name='humanityResult'),
    
    path('humanity/engtest/', views.humanityEngTest, name='humanityEngTest'),
    path('humanity/engsubmit/', views.humanityEngSubmit, name='humanityEngSubmit'),
    path('humanity/engresult/<int:major_id>/', views.humanityEngResult, name='humanityEngResult'),
    
    path('humanity/chtest/', views.humanityCnTest, name='humanityCnTest'),
    path('humanity/chsubmit/', views.humanityCnSubmit, name='humanityCnSubmit'),
    path('humanity/chresult/<int:major_id>/', views.humanityCnResult, name='humanityCnResult'),
    
    path('humanity/board/', views.humanityBoard, name='humanityBoard'),
]