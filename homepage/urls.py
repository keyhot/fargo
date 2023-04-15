from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateMemberView.as_view(), name='member-djangoform'),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
]