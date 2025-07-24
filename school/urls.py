# shop/urls.py
from django.urls import path
from .views import login_view,admin_dashboard,teacher_dashboard,student_dashboard,Subjects_View

urlpatterns = [
    path('', login_view, name='login'),
    path('admin-panel/',admin_dashboard,name='admin-dashboard'),
    path('teacher-panel/',teacher_dashboard,name='teacher-dashboard'),
    path('student-panel/',student_dashboard,name='student-dashboard'),
    path('admin-panel/subjects/',Subjects_View,name='subjects'),
]
