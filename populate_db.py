import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable_api.models import Tutor, Course, Room, Lecture, TimetableSlot

def populate_data():
    # 1. Tutors
    tutors_data = [
        {'name': 'DR. PETER', 'phone': '0706033491', 'unit_code': 'SC102'},
        {'name': 'John Doe', 'phone': '0753672882', 'unit_code': 'SC'},
        {'name': 'Dr. Sanjay Patil', 'phone': '0987654321', 'unit_code': 'CS101'},
        {'name': 'Dr. Anita Deshmukh', 'phone': '0876543210', 'unit_code': 'IT202'},
        {'name': 'Prof. Rajesh Kulkarni', 'phone': '0765432109', 'unit_code': 'CS303'}
    ]
    tutor_objs = {}
    for t_data in tutors_data:
        tutor, created = Tutor.objects.get_or_create(name=t_data['name'], defaults=t_data)
        tutor_objs[t_data['name']] = tutor

    # 2. Rooms
    rooms_data = [
        {'room_no': 'F2', 'capacity': 95, 'name': 'F1.2'},
        {'room_no': 'F1', 'capacity': 80, 'name': 'F1.1'},
        {'room_no': 'RM03', 'capacity': 20, 'name': 'SCIENCE COMPLEX HALL'},
        {'room_no': 'R2', 'capacity': 90, 'name': 'R1.2'},
        {'room_no': 'CNR', 'capacity': 900, 'name': 'CONFERENCE ROOM'}
    ]
    room_objs = {}
    for r_data in rooms_data:
        room, created = Room.objects.get_or_create(room_no=r_data['room_no'], defaults=r_data)
        room_objs[r_data['room_no']] = room

    # 3. Courses
    courses_data = [
        {'code': 'BSC-SE', 'name': 'BSC IN SOFTWARE ENG.', 'department': 'IT', 'year': '1st Year'},
        {'code': 'BSC-IT', 'name': 'BSC IN IT', 'department': 'IT', 'year': '2nd Year'},
        {'code': 'BSC-CS', 'name': 'BSC IN COMPUTER SCIENCE', 'department': 'CS', 'year': '1st Year'}
    ]
    course_objs = {}
    for c_data in courses_data:
        course, created = Course.objects.get_or_create(code=c_data['code'], defaults=c_data)
        course_objs[c_data['name']] = course

    # 4. Lectures
    # Software Eng Schedule Data
    se_schedule_data = [
        { 'tutor': 'DR. PETER', 'subject': 'MACHINE LEARNING', 'room': 'F2' },
        { 'tutor': 'DR. PETER', 'subject': 'COMPUTER SECURITY', 'room': 'F1' },
    ]
    # Simple test data
    for item in se_schedule_data:
        tutor = tutor_objs.get(item['tutor'])
        room = room_objs.get(item['room'])
        lecture, created = Lecture.objects.get_or_create(
            unit_name=item['subject'],
            defaults={
                'unit_code': 'SE101',
                'tutor': tutor,
                'room': room,
                'duration': 1,
                'students': 50
            }
        )
        
        # Add to Timetable for SE
        TimetableSlot.objects.get_or_create(
            course=course_objs['BSC IN SOFTWARE ENG.'],
            day='MON',
            time_slot='8:00-9:00',
            lecture=lecture
        )

    print("Database populated with test data!")

if __name__ == '__main__':
    populate_data()
