from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    #path('bkash/', include('bkash.urls')),
    path('', include('app.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)