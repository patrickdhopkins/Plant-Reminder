from django.contrib import admin
from remindtowater import urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import remindtowater

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('plant/', include(remindtowater.urls)),
    path('registration/', include('registration.urls')),  # new
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
