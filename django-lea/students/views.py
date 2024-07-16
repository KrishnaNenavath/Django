from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    student = Student.objects.all()
    print(student)
    return render(request,'students/index.html', {'student':student} )

def addStudent(request):
    if request.method=='POST':
        print("added")
        Student_roll = request.POST.get("roll")
        Student_name = request.POST.get("name")
        Student_email = request.POST.get("email")
        Student_address = request.POST.get("address")
        Student_phone = request.POST.get("phone")

        s = Student()
        s.roll_number = Student_roll
        s.student_name = Student_name
        s.student_Email = Student_email
        s.student_Address = Student_address
        s.student_phone = Student_phone

        s.save()

        return redirect('/')

    
    return render(request, 'students/add-student.html', {})

def aboutUs(request):
    return render(request, 'students/about.html')