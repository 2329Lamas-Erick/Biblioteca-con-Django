from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from catalogo.views import register


urlpatterns = [
    path('', RedirectView.as_view(url='/catalogo/')),
    path('catalogo/admin/', admin.site.urls),
    path('catalogo/', include('catalogo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
]
