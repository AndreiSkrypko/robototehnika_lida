from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),  # путь при входе в панель администратора
                  path('', include('main_app.urls')),
                  # путь на главную страницу, urls сделан в главном приложении main_app
                  path('forum_list/', include('forum_app.urls')),
                  path('login/', include('login_app.urls')),
                  path('auth/', include('rest_framework.urls')),
                  path('forum/', include('forum_app.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

