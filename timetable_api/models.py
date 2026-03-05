from django.db import models

class Tutor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    unit_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_no = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.room_no

class Lecture(models.Model):
    unit_code = models.CharField(max_length=50)
    unit_name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.IntegerField(default=1)  # in hours
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    students = models.IntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.unit_name

class TimetableSlot(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    time_slot = models.CharField(max_length=50) # e.g., '8:00-9:00'
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.code} - {self.day} - {self.time_slot}"

class AppSettings(models.Model):
    lecture_duration = models.IntegerField(default=1) # in hours
    break_times = models.CharField(max_length=200, default='13:00-14:00')

    def __str__(self):
        return "Global Settings"
