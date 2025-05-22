from django.urls import path
from .views import (
    StudentListCreateAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
    StudentSoftDeleteAPIView
)

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='list-create-students'),
    path('students/update/<int:id>/', StudentUpdateAPIView.as_view(), name='update-student'),
    path('students/delete/<int:id>/', StudentDeleteAPIView.as_view(), name='delete-student'),
    path('students/soft-delete/<int:id>/', StudentSoftDeleteAPIView.as_view(), name='soft-delete-student'),
]
