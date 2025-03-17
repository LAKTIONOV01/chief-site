from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('feedback/', views.CreateContact.as_view(), name='feedback'),
    path('message/', views.ContactView.as_view(), name='message'),
    path('about/', views.AboutView.as_view(), name='about'),

]
