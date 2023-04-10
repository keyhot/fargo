from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from homepage import views

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('admin/clearcache/', include('clearcache.urls')),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
