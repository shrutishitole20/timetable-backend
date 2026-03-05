from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Tutor, Course, Room, Lecture, TimetableSlot, AppSettings
from .serializers import (
    TutorSerializer, CourseSerializer, RoomSerializer,
    LectureSerializer, TimetableSlotSerializer, AppSettingsSerializer
)
import random

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # MAGIC HAPPENS HERE: We create the JWT Tokens for the user!
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'status': 'success',
            'user': user.username,
            'refresh': str(refresh),                  # <-- Your Refresh Token!
            'access': str(refresh.access_token),      # <-- Your Access Token!
        })
    else:
        return Response({'status': 'error', 'message': 'Invalid username or password'}, status=401)
    
    
@api_view(['POST'])
def signup_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'status': 'error', 'message': 'User already exists'}, status=400)
    user = User.objects.create_user(username, email, password)
    return Response({'status': 'success', 'user': user.username})

# 3. THE LOGOUT WAITER
@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 'success', 'message': 'Logged out successfully!'})


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class TimetableSlotViewSet(viewsets.ModelViewSet):
    queryset = TimetableSlot.objects.all()
    serializer_class = TimetableSlotSerializer

    def get_queryset(self):
        queryset = TimetableSlot.objects.all()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    @action(detail=False, methods=['post'])
    def generate(self, request):
        course_id = request.data.get('course_id')
        if not course_id:
            return Response({'error': 'course_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        # Clear existing slots for this course
        TimetableSlot.objects.filter(course=course).delete()

        # Get lectures specifically for this course
        lectures = list(Lecture.objects.filter(course=course))
        if not lectures:
            return Response({'error': f'No lectures assigned to {course.name}. Please add lectures first.'}, status=status.HTTP_400_BAD_REQUEST)

        days = ['MON', 'TUE', 'WED', 'THU', 'FRI']
        time_slots = [
            '8:00-9:00', '9:00-10:00', '10:00-11:00', '11:00-12:00',
            '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00'
        ]

        # Improved generation: Assign lectures to slots
        # For each lecture, try to find a random free slot
        available_slots = [(d, t) for d in days for t in time_slots]
        random.shuffle(available_slots)

        for lecture in lectures:
            # If a lecture lasts for 1 hour, it takes 1 slot
            # For simplicity, we assign 1 slot per lecture entry
            if available_slots:
                day, slot = available_slots.pop()
                TimetableSlot.objects.create(
                    course=course,
                    day=day,
                    time_slot=slot,
                    lecture=lecture
                )

        return Response({'status': 'Timetable generated successfully', 'count': len(lectures)})

class AppSettingsViewSet(viewsets.ModelViewSet):
    queryset = AppSettings.objects.all()
    serializer_class = AppSettingsSerializer

    def list(self, request, *args, **kwargs):
        # We only want one settings object
        settings = AppSettings.objects.first()
        if not settings:
            settings = AppSettings.objects.create()
        serializer = self.get_serializer(settings)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def save_settings(self, request):
        settings = AppSettings.objects.first()
        if not settings:
            settings = AppSettings.objects.create()
        
        serializer = self.get_serializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
