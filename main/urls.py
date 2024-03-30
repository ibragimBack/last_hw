from django.contrib import admin
from django.urls import path
from django.conf.urls.static import (static)
from django.conf import settings
from book.views import post_library_view, post_librarys_detail_view
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', post_library_view),
    path('book/<int:id>/', post_librarys_detail_view),
    path('^i18n/', include('django.conf.urls.i18n')),
    path('', include('book_forum.urls')),
    path('', include('parser.urls')),
    path('', include('custom_users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
