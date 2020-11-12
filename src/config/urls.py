from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include ("django.contrib.auth.urls")),
    path('accounts/', include ("users.urls")),
    path("", include("core.urls"))
    #Local
    # path('home/', core_views.home),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                            document_root=settings.MEDIA_ROOT)































