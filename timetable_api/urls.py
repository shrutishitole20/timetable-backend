from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    TutorViewSet, CourseViewSet, RoomViewSet,
    LectureViewSet, TimetableSlotViewSet, AppSettingsViewSet,
    login_view, signup_view, logout_view
)

router = DefaultRouter()
router.register(r'tutors', TutorViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'lectures', LectureViewSet)
router.register(r'timetable-slots', TimetableSlotViewSet)
router.register(r'settings', AppSettingsViewSet)

urlpatterns = [
    path('login/', login_view),
    path('signup/', signup_view),
    path('logout/', logout_view),
    path('token/refresh/', TokenRefreshView.as_view()),  # JWT token refresh
    path('', include(router.urls)),
]

