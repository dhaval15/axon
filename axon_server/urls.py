from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('orgroam/', include('orgroam.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
