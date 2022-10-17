from django.urls import path
from it import views

urlpatterns = [
	path('it/test/', views.itTest, name='itTest'),
    path('it/submit/', views.itSubmit, name='itSubmit'),
    path('it/result/<int:major_id>/', views.itResult, name='itResult'),
    
    path('it/engtest/', views.itEngTest, name='itEngTest'),
    path('it/engsubmit/', views.itEngSubmit, name='itEngSubmit'),
    path('it/engresult/<int:major_id>/', views.itEngResult, name='itEngResult'),
    
    path('it/chtest/', views.itChTest, name='itChTest'),
    path('it/chsubmit/', views.itChSubmit, name='itChSubmit'),
    path('it/chresult/<int:major_id>/', views.itChResult, name='itChResult'),
    
    path('it/board/', views.itboard, name='itBoard'),
]