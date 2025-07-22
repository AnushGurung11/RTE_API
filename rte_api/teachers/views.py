from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd

from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class UploadTeacherExcelView(APIView):
    def post(self, request, *args, **kwargs):
        excel_file = request.FILES.get('excel')
        if not excel_file:
            return Response({"error": "Excel file pathaunus"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            all_sheets = pd.read_excel(excel_file, sheet_name=None)
            teachers = []

            for sheet_name, df in all_sheets.items():
                required_columns = {'name', 'email'}
                if not required_columns.issubset(df.columns):
                    continue

                for _, row in df.iterrows():
                    teacher = Teacher(
                        full_name=row['name'],
                        email=row['email']
                    )
                    teachers.append(teacher)

            Teacher.objects.bulk_create(teachers)
            return Response(
                {"message": f"{len(teachers)} teachers uploaded from {len(all_sheets)} sheets."},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
