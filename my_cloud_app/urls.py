from django.urls import path, include
from .views import login_user, logout_user, register_user, list_users, delete_user, get_list_files, \
    delete_file, get_list_files_admin, upload_file, rename_file, edit_description_file, download_file, \
    download_file_from_link, creating_link_to_the_file, edit_user


urlpatterns = [
    # Административные маршруты
    path('admin/get_users/', list_users),
    path('admin/edit_user/', edit_user),
    path('admin/delete_user/', delete_user),
    path('admin/get_user_files/', get_list_files_admin),
    path('admin/get_users/', list_users, name='admin-get-users'),

    # Работа с файлами
    path('upload_file/', upload_file),
    path('get_files/', get_list_files),
    path('delete_file/', delete_file),
    path('edit_description_file/', edit_description_file),
    path('rename_file/', rename_file),
    path('download_file/', download_file),

    # Публичные маршруты
    path('public/download_file_from_link/', download_file_from_link),
    path('public/download_file/', download_file_from_link),
    path('creating_link_to_the_file/', creating_link_to_the_file),
    
    # Аутентификация
    path('login/', login_user),
    path('logout/', logout_user),
    path('register/', register_user),
    path('login/', login_user, name='login'),
]

