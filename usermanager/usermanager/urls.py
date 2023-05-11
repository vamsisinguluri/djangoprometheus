from django.contrib import admin
from django.urls import path, include
from userapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),
    path('users/', views.UsersView.as_view()),
    path('health/', views.HealthCheck.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
