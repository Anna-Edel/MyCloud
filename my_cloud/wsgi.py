"""
WSGI конфигурация для проекта MyCloud.

Этот файл предоставляет объект WSGI, доступный как переменная уровня модуля с именем ``application``.

Для получения дополнительной информации об этом файле см. документацию:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_cloud.settings')

application = get_wsgi_application()
