from django.contrib import admin
from django.urls import path
import articles.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles.views.home, name='home'),
    path('news/<int:article_id>', articles.views.detail, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)