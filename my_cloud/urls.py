"""
Конфигурация URL для проекта MyCloud.

Список `urlpatterns` связывает URL-адреса с представлениями (views). Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Примеры:
Функции-представления:
    1. Добавьте импорт:  from my_app import views
    2. Добавьте URL в urlpatterns:  path('', views.home, name='home')

Классы-представления:
    1. Добавьте импорт:  from other_app.views import Home
    2. Добавьте URL в urlpatterns:  path('', Home.as_view(), name='home')

Подключение другого URLconf:
    1. Импортируйте функцию include(): from django.urls import include, path
    2. Добавьте URL в urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Путь для административной панели
    path('admin/', admin.site.urls),
    # Путь для API приложения my_cloud_app
    path('api/', include('my_cloud_app.urls')),
]