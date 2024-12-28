from django.shortcuts import render
from django.http import request , JsonResponse
from .models import Student
from .serilizers import StudentSerialiser
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.
@csrf_exempt
def student_api(request,pk=None):
    if request.method =='GET':
        if pk is not None :
            stu = Student.objects.get(id=pk)
            serialize = StudentSerialiser(stu)
            return JsonResponse(serialize.data)
        stu = Student.objects.all()
        serialize = StudentSerialiser(stu, many=True)
        #print(serialize.data)
        return JsonResponse(serialize.data, safe= False)
    
    if request.method == 'POST':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream=stream)
            serializer = StudentSerialiser(data= pythondata)
            if serializer.is_valid():
                serializer.save()
                resp = {'msg':'Data created successfully'}
                return JsonResponse(resp,status =201)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
                return JsonResponse({'error': 'Invalid request: ' + str(e)}, status=400)
    if request.method == 'PUT':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream=stream)
            # Extract 'id' or 'roll' from the request
            student_id = pythondata.get('id')
            student_roll = pythondata.get('roll')
            if student_id:
                stu = Student.objects.get(id=student_id)  # Update by ID
            elif student_roll:
                stu = Student.objects.get(roll=student_roll)  # Update by Roll
            else:
                return JsonResponse({'error': 'ID or Roll number must be provided.'}, status=400)
            
            serializer = StudentSerialiser(stu , data= pythondata , partial=True)
            if serializer.is_valid():
                serializer.save()
                resp = {'msg':'Data updated successfully'}
                return JsonResponse(resp,status =201)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Invalid request: ' + str(e)}, status=400)

    if request.method == 'DELETE':
        try:
            json_data = request.body
            print (json_data)
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream=stream)

            
            # Extract 'id' or 'roll' from the request
            student_id = pythondata.get('id')
            student_roll = pythondata.get('roll')
            
            if student_id:
                stu = Student.objects.get(id=student_id)  # Delete by ID
            elif student_roll:
                stu = Student.objects.get(roll=student_roll)  # Delete by Roll
            else:
                return JsonResponse({'error': 'ID or Roll number must be provided.'}, status=400)
            stu.delete()
            resp = {'msg': 'Data deleted successfully!'}
            return JsonResponse(resp, status=200)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Invalid request: ' + str(e)}, status=400)