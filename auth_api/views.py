from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
import logging

logger = logging.getLogger('Inventory management system')

class AuthRegister(APIView):
    permission_classes = [AllowAny]
    def post(self,request):

        username = request.data.get('username',None)
        password = request.data.get('password',None)
        email = request.data.get('email',None)
        first_name = request.data.get('first_name',None)
        last_name = request.data.get('last_name',None)
        logger.info(f"Response Data: {request.data}")
        if len(request.data)>0:
            if username is None:
                return Response({'message':'Please Enter Username'}, status=status.HTTP_400_BAD_REQUEST)
            elif password is None:
                return Response({'message':'Please Enter Password'}, status=status.HTTP_400_BAD_REQUEST)
            elif email is None:
                return Response({'message':'Please Enter email address'}, status=status.HTTP_400_BAD_REQUEST)
            
            User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            return Response({"Message":"User Created Successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message':'Please Add Valid Data.'},status=status.HTTP_400_BAD_REQUEST)