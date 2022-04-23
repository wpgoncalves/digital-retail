from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from about.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', RedirectView.as_view(url='admin/'), name='admin'),
    path('showcase/', include('showcase.urls')),
    path('about/', about, name='about'),
    path('', RedirectView.as_view(url='showcase/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
