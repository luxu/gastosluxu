from django.conf import settings
from django.urls import path, include
from django.contrib import admin
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('website.urls')),
]
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]