"""
ASGI конфигурация для проекта MyCloud.

Этот файл предоставляет ASGI объект, доступный как переменная уровня модуля с именем ``application``.

Для получения дополнительной информации о данном файле см. документацию:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_cloud.settings')

application = get_asgi_application()
