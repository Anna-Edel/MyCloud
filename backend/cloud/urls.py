from django.urls import path
from .views import RegisterView, LoginView, LogoutView, FileListView, FileUploadView, FileDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('files/', FileListView.as_view(), name='file_list'),
    path('files/upload/', FileUploadView.as_view(), name='file_upload'),
    path('files/<int:pk>/delete/', FileDeleteView.as_view(), name='file_delete'),
]