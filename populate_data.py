
import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable_api.models import Tutor, Course, Room, Lecture, TimetableSlot

def populate():
    print("Starting population script...")

    # 1. Create Tutors if they don't exist
    tutor_names = [
        "Dr. Smith", "Prof. Johnson", "Dr. Williams", "Ms. Brown", 
        "Mr. Jones", "Dr. Garcia", "Prof. Miller", "Dr. Davis"
    ]
    tutors = []
    for name in tutor_names:
        tutor, created = Tutor.objects.get_or_create(
            name=name,
            defaults={'phone': f"555-{random.randint(1000, 9999)}", 'unit_code': f"CS{random.randint(100, 400)}"}
        )
        tutors.append(tutor)
    print(f"Ensured {len(tutors)} tutors.")

    # 2. Create Courses
    course_data = [
        ("CS101", "Computer Science", "Engineering", "Year 1"),
        ("IT202", "Information Technology", "IT Dept", "Year 2"),
        ("EE303", "Electrical Engineering", "Engineering", "Year 3"),
        ("ME404", "Mechanical Engineering", "Engineering", "Year 4"),
        ("BA505", "Business Administration", "Business", "Year 1"),
    ]
    courses = []
    for code, name, dept, year in course_data:
        course, created = Course.objects.get_or_create(
            code=code,
            defaults={'name': name, 'department': dept, 'year': year}
        )
        courses.append(course)
    print(f"Ensured {len(courses)} courses.")

    # 3. Create Rooms
    room_data = [
        ("R101", 30, "Main Hall"),
        ("R102", 20, "Lab A"),
        ("R201", 40, "Lecture Theater"),
        ("R202", 25, "Seminar Room"),
        ("R301", 35, "CS Lab"),
    ]
    rooms = []
    for no, cap, name in room_data:
        room, created = Room.objects.get_or_create(
            room_no=no,
            defaults={'capacity': cap, 'name': name}
        )
        rooms.append(room)
    print(f"Ensured {len(rooms)} rooms.")

    # 4. Create Lectures for each course
    # Each course should have several units
    units = {
        "CS101": ["Programming Basics", "Data Structures", "Web Dev", "Algorithms", "Databases"],
        "IT202": ["Network Security", "Cloud Computing", "UI/UX Design", "E-commerce", "Operating Systems"],
        "EE303": ["Circuit Analysis", "Digital Electronics", "Power Systems", "Control Systems", "Microprocessors"],
        "ME404": ["Thermodynamics", "Fluid Mechanics", "Machine Design", "Manufacturing", "Robotics"],
        "BA505": ["Marketing", "Accounting", "HR Management", "Economics", "Business Ethics"]
    }

    for course in courses:
        course_units = units.get(course.code, ["General Unit 1", "General Unit 2"])
        for unit_name in course_units:
            Lecture.objects.get_or_create(
                unit_name=unit_name,
                course=course,
                defaults={
                    'unit_code': f"{course.code}-{unit_name[:3].upper()}",
                    'duration': random.randint(1, 2),
                    'tutor': random.choice(tutors),
                    'students': random.randint(15, 40),
                    'room': random.choice(rooms)
                }
            )
    print("Created lectures for all courses.")

    # 5. Generate Timetable Slots (Trigger the logic from the viewset)
    from timetable_api.views import TimetableSlotViewSet
    from rest_framework.test import APIRequestFactory

    factory = APIRequestFactory()
    view = TimetableSlotViewSet.as_view({'post': 'generate'})

    for course in courses:
        request = factory.post('/api/timetable-slots/generate/', {'course_id': course.id}, format='json')
        response = view(request)
        if response.status_code == 200:
            print(f"Generated timetable for {course.name}")
        else:
            print(f"Failed to generate for {course.name}: {response.data}")

    print("Population complete!")

if __name__ == "__main__":
    populate()
