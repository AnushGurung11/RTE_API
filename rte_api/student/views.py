from rest_framework import viewsets,status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UploadExcelView(APIView):
    
    # This will Handle the post 
    
    def post(self, request, *args, **kwargs):
        # Yho wala file name lai linxa
        excel_file = request.FILES.get('excel')
        
        try:
            # Yesh le chai read garxa file lai
            all_sheets = pd.read_excel(excel_file, sheet_name=None)
            
            # Yesh ma temporary storage hunxa
            students = []
            
            # sheet_name le pachi year lai extract garxa and df le data lai read garxa
            for sheet_name, df in all_sheets.items():
                try:
                    # Sheet ko name bata number lai nikal xa 
                    year = int(''.join(filter(str.isdigit, sheet_name)))
                except:
                    # yedi number paye na vane default 1 hunxa value
                    year = 1  

                # Column name ko basis read garxa 
                required_columns = {'lmu_id', 'name', 'section', 'intake', 'course'}
                if not required_columns.issubset(df.columns):
                    continue  

                for _, row in df.iterrows():
                    student = Student(
                        lmu_id=row['lmu_id'],
                        student_name=row['name'],
                        section=row['section'],
                        intake=row['intake'],
                        course=row['course'],
                        year=year
                    )
                    students.append(student)

            Student.objects.bulk_create(students)
            return Response({"message": f"{len(students)} students uploaded from {len(all_sheets)} sheets."}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
        

class StudentInfo(APIView):
    """
    This call is related to student info gathering
    """
    
    def get(self):
        """
        This function will get the student info
        """
        
        students = Student.objects.values('lmu_id','student_name','section')
        return Response(students)
        
        
    