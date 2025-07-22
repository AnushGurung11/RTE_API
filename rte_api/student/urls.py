from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, UploadExcelView  # Your views here

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-excel/', UploadExcelView.as_view(), name='upload-excel'),
]
