from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, logout
from .models import CloudUser, CloudFile
from .serializers import UserSerializer, LoginSerializer, CloudFileSerializer

# Регистрация пользователя
class RegisterView(generics.CreateAPIView):
    queryset = CloudUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Аутентификация (вход)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"message": "Успешный вход"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Выход из системы
class LogoutView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({"message": "Выход выполнен"}, status=status.HTTP_200_OK)

# Получение списка файлов
class FileListView(generics.ListAPIView):
    serializer_class = CloudFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            user_id = self.request.query_params.get('user_id')
            if user_id:
                return CloudFile.objects.filter(user__id=user_id)
            return CloudFile.objects.all()
        return CloudFile.objects.filter(user=user)

# Загрузка файла
class FileUploadView(generics.CreateAPIView):
    serializer_class = CloudFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        file_obj = self.request.FILES.get('file')
        if not file_obj:
            raise serialzers.ValidationError("Файл не найден в запросе")
        serializer.save(
            user=self.request.user,
            original_name=file_obj.name,
            size=file_obj.size,
            file=file_obj
        )

# Удаление файла
class FileDeleteView(generics.DestroyAPIView):
    serializer_class = CloudFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CloudFile.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Разрешаем удалить, если пользователь — администратор или владелец файла
        if self.request.user.is_staff or obj.user == self.request.user:
            return obj
        raise PermissionDenied("Нет прав для удаления этого файла.")
