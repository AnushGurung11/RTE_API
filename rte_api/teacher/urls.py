from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet,UploadExcelView,TeacherInfo

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-excel/', UploadExcelView.as_view(), name='upload-excel'),
    path('get-info/',TeacherInfo.as_view(),name='teachers-info'),
]
