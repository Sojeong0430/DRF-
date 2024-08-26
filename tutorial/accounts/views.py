from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, LoginSerializer
from django.contrib.auth.models import User
from .models import JWT
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , login, logout
from .utils import get_access_token , get_refresh_token
#from rest_framework.permissions import AllowAny

class UserRegisterView(APIView):
      def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class UserlistView(APIView):
    def get(self,request):
        queryset = User.objects.all()
        serializer = UserRegistrationSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class LoginAPI(APIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password'),
        )
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,data={"message":"입력하신 정보가 올바르지 않습니다"})
        
        access = get_access_token({"user_id":user.id}) #암호화가 되어있고, 유저정보를 담고 있다
        refresh = get_refresh_token()

        JWT.objects.create(
            user=user,
            access=access,
            refresh = refresh,
        )

        #세션 로그인
        login(request, user)

        response = Response(status=status.HTTP_200_OK)
        data = {
            "access":access,
        }

        response.data = data
        response.set_cookie(key='access',value=access)
        response.set_cookie(key='refresh',value=refresh,httponly=True)

        return response
    



class LogoutAPI(APIView):

    def get(self,request):

        #jwt 토큰 삭제

        #세션로그아웃
        logout(request)
        #쿠키삭제
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie("access")
        response.delete_cookie("refresh")

        return response

