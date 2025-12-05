from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    
    POST /api/auth/register/
    {
        "username": "johndoe",
        "email": "john@example.com",
        "password": "securepassword123",
        "password2": "securepassword123",
        "first_name": "John",  // optional
        "last_name": "Doe"     // optional
    }
    
    Returns:
    {
        "user": {
            "id": 1,
            "username": "johndoe",
            "email": "john@example.com"
        },
        "token": "a1b2c3d4e5f6...",
        "message": "User registered successfully"
    }
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create authentication token for the new user
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """
    API endpoint for user login.
    
    POST /api/auth/login/
    {
        "username": "johndoe",
        "password": "securepassword123"
    }
    
    Returns:
    {
        "token": "a1b2c3d4e5f6...",
        "user_id": 1,
        "username": "johndoe",
        "email": "john@example.com"
    }
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Get or create token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
    API endpoint for user logout.
    Deletes the user's authentication token.
    
    POST /api/auth/logout/
    Headers: Authorization: Token a1b2c3d4e5f6...
    
    Returns:
    {
        "message": "Successfully logged out"
    }
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Delete the user's token
            request.user.auth_token.delete()
            return Response({
                'message': 'Successfully logged out'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to view and update user profile.
    
    GET /api/auth/profile/
    Returns current user's profile
    
    PUT/PATCH /api/auth/profile/
    Update current user's profile
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
