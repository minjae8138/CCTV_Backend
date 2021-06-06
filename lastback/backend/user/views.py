# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.serializer import UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
@api_view(['POST'])
def makeId(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("error")
    return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET'])
def infoGet(request):
    print(request)
    return Response(request.data)
