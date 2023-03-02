from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.CreateMemberView.as_view(), name='member-djangoform'),
]