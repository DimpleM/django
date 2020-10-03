from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token  
from api.serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from  rest_framework import filters


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserAuthentication(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user = user)
        return Response(token.key)

class Register(APIView):
    permission_classes = [AllowAny, ]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class Profiles(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request,  format=None):
        username = request.user.username
        user = User.objects.get(username=username)
        model = Profile.objects.get(user=user)
        try:
            serializer = ProfileSerializer(instance=model)

            return Response(serializer.data) 
        except:
            error = "Profile Does Not exists"
            return Response(error, status= status.HTTP_400_BAD_REQUEST)

class AddFriend(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request, format=None):
        try:
            if 'username' in request.data:
                username = request.user.username
                user = User.objects.get(username=username)
                profile = Profile.objects.get(user=user)
                user = User.objects.get(username=request.data['username'])
                profile1 = Profile.objects.get(user=user)
                profile.friends.add(profile1)
                return Response("Friend Added!")
            else:
                return Response("Please enter the username", status= status.HTTP_400_BAD_REQUEST)
        except:
                return Response("Some Error occured..Please check..", status= status.HTTP_400_BAD_REQUEST)


class DeleteFriend(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request, format=None):
        try:
            if 'username' in request.data:
                username = request.user.username
                user = User.objects.get(username=username)
                profile = Profile.objects.get(user=user)
                user = User.objects.get(username=request.data['username'])
                profile1 = Profile.objects.get(user=user)
                profile.friends.remove(profile1)
                return Response("Friend Removed!")
            else:
                return Response("Please enter the username", status= status.HTTP_400_BAD_REQUEST)
        except:
                return Response("Some Error occured..Please check..", status= status.HTTP_400_BAD_REQUEST)



class AllProfiles(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request,  format=None):
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            model = Profile.objects.exclude(user=user)
            request = Profile.objects.get(user=user)
            serializer =ProfileSerializer(instance=model, many=True,context= {"profile":request})
            return Response(serializer.data) 
        except:
            error = "Profile Does Not exists"
            return Response(error, status= status.HTTP_400_BAD_REQUEST)
    
class  ProfileSearch(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        profiles = Profile.objects.all()
        city = self.request.query_params.get('city', None)
        gender = self.request.query_params.get('gender', None)
        queryset1 = ''
        if gender is not None:
            queryset1 = profiles.filter(gender=gender)
        if city is not None:
            queryset1 = profiles.filter(perAddress__in=Address.objects.filter(city=city))
        serializer_class = ProfileSerializer(queryset1,many=True)
        return Response(serializer_class.data)



