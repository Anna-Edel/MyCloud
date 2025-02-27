import os
import sys

def main():
    """Запуск административных задач."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycloud.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен и доступен в PYTHONPATH, "
            "а также что виртуальное окружение активировано."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
