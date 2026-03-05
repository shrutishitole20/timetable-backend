from rest_framework import serializers
from .models import Tutor, Course, Room, Lecture, TimetableSlot, AppSettings

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    tutor_name = serializers.ReadOnlyField(source='tutor.name')
    room_name = serializers.ReadOnlyField(source='room.name')
    course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = Lecture
        fields = '__all__'

class TimetableSlotSerializer(serializers.ModelSerializer):
    lecture_name = serializers.ReadOnlyField(source='lecture.unit_name')
    tutor_name = serializers.ReadOnlyField(source='lecture.tutor.name')
    room_name = serializers.ReadOnlyField(source='lecture.room.name')
    course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = TimetableSlot
        fields = '__all__'

class AppSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSettings
        fields = '__all__'
