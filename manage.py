#!/usr/bin/env python
"""Утилита командной строки Django для выполнения административных задач."""
import os
import sys


def main():
    """Запуск административных задач."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_cloud.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что оно установлено и доступно"
            "в вашей переменной окружения PYTHONPATH."
            "Вы случайно не забыли активировать виртуальное окружение?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()