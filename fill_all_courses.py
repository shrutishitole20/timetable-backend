
import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable_api.models import Course, Lecture, Tutor, Room, TimetableSlot
from timetable_api.views import TimetableSlotViewSet
from rest_framework.test import APIRequestFactory

def fill_all():
    print("🚀 Starting comprehensive population for all courses...")
    
    courses = Course.objects.all()
    tutors = list(Tutor.objects.all())
    rooms = list(Room.objects.all())
    
    if not tutors:
        tutors = [Tutor.objects.create(name="Lead Professor")]
    if not rooms:
        rooms = [Room.objects.create(room_no="Main Hall", capacity=100)]

    # Expanded list of subjects to pull from
    subject_pool = [
        "Mathematics I", "Physics for Engineers", "Communication Skills", 
        "Ethics in Tech", "Project Management", "Cyber Security", 
        "Data Analytics", "Mobile App Development", "High Performance Computing",
        "Natural Language Processing", "Cloud Architecture", "Interaction Design",
        "History of Science", "Environmental Studies", "Technical Writing",
        "Entrepreneurship", "Strategic Management", "Finance for Engineers",
        "Embedded Systems", "VLSI Design", "Strength of Materials",
        "Heat Transfer", "Industrial Automation", "Supply Chain Design"
    ]

    factory = APIRequestFactory()
    view = TimetableSlotViewSet.as_view({'post': 'generate'})

    for course in courses:
        print(f"--- Processing: {course.name} ({course.code}) ---")
        
        # Check current lecture count
        current_lectures = Lecture.objects.filter(course=course).count()
        
        # Add lectures until we have at least 15 for a very full schedule
        to_add = max(0, 15 - current_lectures)
        
        for i in range(to_add):
            unit_name = random.choice(subject_pool) + f" {random.randint(1, 100)}"
            Lecture.objects.create(
                unit_name=unit_name,
                unit_code=f"{course.code[:3].upper()}{random.randint(100, 999)}",
                course=course,
                duration=1,
                tutor=random.choice(tutors),
                students=random.randint(20, 50),
                room=random.choice(rooms)
            )
        
        print(f"  Result: {Lecture.objects.filter(course=course).count()} total lectures.")
        
        # Generate the timetable slots
        request = factory.post('/api/timetable-slots/generate/', {'course_id': course.id}, format='json')
        response = view(request)
        if response.status_code == 200:
            print(f"  ✅ Generated {response.data.get('count')} slots in the grid.")
        else:
            print(f"  ❌ Generation failed: {response.data}")

    print("\n✨ All courses are now fully populated and scheduled!")

if __name__ == "__main__":
    fill_all()
