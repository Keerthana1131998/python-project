from django.urls import path

from . import views

urlpatterns =[ 
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),
    path('dashboard',views.dashboard,name='dashboard'),
    
]