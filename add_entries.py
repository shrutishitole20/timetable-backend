
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable_api.models import Course, Lecture, Tutor, Room, TimetableSlot
from timetable_api.views import TimetableSlotViewSet
from rest_framework.test import APIRequestFactory

def add_entries():
    course = Course.objects.filter(id=1).first()
    if not course:
        print("Course 1 not found")
        return

    tutors = list(Tutor.objects.all())
    rooms = list(Room.objects.all())

    if not tutors:
        tutors = [Tutor.objects.create(name="Prof. Alan Turing")]
    if not rooms:
        rooms = [Room.objects.create(room_no="F1.1", capacity=40)]

    new_units = [
        "Object Oriented Programming",
        "Database Systems",
        "Discrete Mathematics",
        "Web Technologies",
        "Software Engineering",
        "Operating Systems",
        "Computer Networks",
        "Artificial Intelligence",
        "Digital Logic Design"
    ]

    for unit in new_units:
        Lecture.objects.get_or_create(
            unit_name=unit,
            course=course,
            defaults={
                'unit_code': unit[:3].upper() + "202",
                'duration': 1,
                'tutor': tutors[len(unit) % len(tutors)],
                'students': 35,
                'room': rooms[len(unit) % len(rooms)]
            }
        )
    
    # Trigger generation
    factory = APIRequestFactory()
    view = TimetableSlotViewSet.as_view({'post': 'generate'})
    request = factory.post('/api/timetable-slots/generate/', {'course_id': course.id}, format='json')
    response = view(request)
    
    print(f"Status: {response.status_code}")
    print(f"Message: {response.data}")

if __name__ == "__main__":
    add_entries()
