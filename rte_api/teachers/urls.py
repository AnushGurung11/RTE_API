from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teachers.views import TeacherViewSet, UploadTeacherExcelView

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-teachers/', UploadTeacherExcelView.as_view(), name='upload-teachers'),
]
