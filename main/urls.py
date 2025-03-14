from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
]
