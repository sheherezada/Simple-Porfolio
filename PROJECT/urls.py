from PROJECT.accounts.views import logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PROJECT.web.urls')),
    path('accounts/', include('PROJECT.accounts.urls')),
    path('logout/', logout, name='logout'),
    path('profile/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)