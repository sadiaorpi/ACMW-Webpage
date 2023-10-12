from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import PhotoUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('resources/', TemplateView.as_view(template_name='resources.html'), name='resources'),
    path('calendar/', TemplateView.as_view(template_name='calendar.html'), name='calendar'),
    path('photos/', PhotoUploadView.as_view(), name='photo_upload'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


