from rest_framework import viewsets,status
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class UploadExcelView(APIView):
    
    # This will Handle the post 
    
    def post(self, request, *args, **kwargs):
        # Yho wala file name lai linxa
        excel_file = request.FILES.get('excel')
        
        try:
            # Yesh le chai read garxa file lai
            all_sheets = pd.read_excel(excel_file,sheet_name=None)
            
            # Yesh ma temporary storage hunxa
            teachers = []
            
            # sheet_name le pachi year lai extract garxa and df le data lai read garxa
            for sheet_name,df in all_sheets.items():
                
                # Column name ko basis read garxa 
                required_columns = {'teacher_id', 'teacher_name', 'email'}
                if not required_columns.issubset(df.columns):
                    continue  

                for _, row in df.iterrows():
                    teacher = Teacher(
                        teacher_id=row['teacher_id'],
                        teacher_name=row['teacher_name'],
                        email=row['email'],
                        
                    )
                    teachers.append(teacher)

            Teacher.objects.bulk_create(teachers)
            return Response({"message": f"{len(teachers)} teachers uploaded from {len(all_sheets)} sheets."}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
        
class TeacherInfo(APIView):
    
    def get(self):
        
        teachers = Teacher.objects.values('teacher_name','email')
        return Response(teachers)    