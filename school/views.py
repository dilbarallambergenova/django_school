from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from school.models import CustomUser,Subject

def login_view(request):
            
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)
            if request.user.role=='admin':
              return redirect('admin-dashboard')
            elif request.user.role=='teacher':
              return redirect('teacher_dashboard')
            elif request.user.role=='student':
              return redirect('student_dashboard')
       
            
        else:
            return render(request,'login.html',{'error':"Login yoki parol no'togri"})
    return render(request,'login.html')
@login_required
def admin_dashboard(request):
    return render(request,'admin-dashboard.html')
    
@login_required
def teacher_dashboard(request):
    return render(request,'teacher-dashboard.html')
    
@login_required
def student_dashboard(request):
    return render(request,'student-dashboard.html')

def Subjects_View(request):
  subjects=Subject.objects.prefetch_related('teachers').all()
  context={
    'subjects':subjects
  }
  return render(request,'subjects.html',context)

