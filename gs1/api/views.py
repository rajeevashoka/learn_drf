from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#Model Object - Single Student Data
def student_detail(request,pk):
    try:
        stu = Student.objects.get(id=pk)  # Fetch student with matching ID
        serializer = StudentSerializer(stu)  # Serialize student data
        #json_data = JSONRenderer().render(serializer.data)    #--1

        # Debugging Output
        print("stu:", stu)
        print("serializer:", serializer)
        print("serializer.data:", serializer.data)
        #print("json_data:", json_data, type(json_data))

        #return HttpResponse(json_data, content_type='application/json') #--2
        return JsonResponse(serializer.data)    # =1+2

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

#Queryset- all Student Data
def student_list(request):
    stu = Student.objects.all()   #  complex data
    serializer = StudentSerializer(stu, many=True)   # python data 
    #json_data = JSONRenderer().render(serializer.data)
    print ("stu",stu)
    print ("serializer",serializer)
    print ("serializer.data",serializer.data)
    #print ("json_data",json_data,type(json_data))
    #return HttpResponse(json_data , content_type= 'application/json')
    return JsonResponse(serializer.data, safe= False)    # =1+2   # for non-dict dat-->  safe= False