from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import io
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        try:
            jsondata = request.body  # Raw JSON data from the request
            stream = io.BytesIO(jsondata)  # Convert JSON data to a stream
            python_data = JSONParser().parse(stream=stream)  # Parse the stream into Python data
            serializer = StudentSerializer(data = python_data)  # Deserialize the Python data
            if serializer.is_valid():   # Validate the data
                serializer.save()       # Save the valid data to the database
                res = {'msg':'Data created successfully', 'status':201}
                #json_data= JSONRenderer().render(res)   #-->1
                #return HttpResponse(json_data, content_type='application/json')  #-->2
                return JsonResponse(res, status=201)  #==-->1+2
            
            # Return validation errors if the serializer is not valid
            return JsonResponse(serializer.errors, status=400)   #==-->1+2
            
        except IntegrityError as e:
                if 'unique constraint' in str(e).lower():
                    return JsonResponse({'error': 'Roll number must be unique'}, status=400)
                return JsonResponse({'error': 'Database error: ' + str(e)}, status=500)
            
        except Exception as e:
                return JsonResponse({'error': 'Invalid request: ' + str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)