from django.urls import path
from .views import Home, StudentDetailView, StudentListView, StudentUpdateView, StudentDeleteView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('student_delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
]
