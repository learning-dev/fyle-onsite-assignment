from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('api/branches/autocomplete', views.get_branches_autocomplete, name='autocomplete'),
    path('api/branches/', views.get_branches, name='branches'),
]
