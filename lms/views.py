from django.shortcuts import render, redirect
from .models import Student, Books
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password, check_password
User.objects.all()

def admin(request):
    return render(request,'admin.html')

def home(request):
    return render(request,'home.html')

def register_student(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        email_id = request.POST.get("email_id")
        contact_number = request.POST.get("contact_number")
        date_of_birth = request.POST.get("date_of_birth")
        city = request.POST.get("city")
        course_enrolled = request.POST.get("course_enrolled")
        enrollment_date = request.POST.get("enrollment_date")


        # Check for duplicate email
        if Student.objects.filter(email_id=email_id).exists():
            messages.error(request, "Email ID already exists!")
            return redirect("register_student")

        # Create and save new students
        Student.objects.create(
            student_name=student_name,
            email_id=email_id,
            contact_number=contact_number,
            date_of_birth=date_of_birth,
            city=city,
            course_enrolled =course_enrolled,
            enrollment_date =enrollment_date,
        )
        messages.success(request, "Students registered successfully!")
        return redirect("register_student")

    return render(request, "register.html")

def list_student(request):
    students = Student.objects.all()  # Retrieve all students
    return render(request, "list.html", {"students": students})

def delete_student(request,student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    messages.success(request, "Students deleted successfully!")
    return redirect("list_student")

def update_student(request,student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, "update.html", {"student": student})

def uprec(request, student_id):
    id = request.POST['student_id']
    name = request.POST['student_name']
    email = request.POST['email_id']
    contact = request.POST['contact_number']
    city = request.POST['city']
    course_enrolled = request.POST['course_enrolled']
    student = Student.objects.get(pk=id)
    student.name = name
    student.email_id = email
    student.contact_number = contact
    student.city = city
    student.course_enrolled = course_enrolled
    student.save()
    messages.success(request, "Students updated successfully!")
    return redirect("list_student")



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")
        # Save user to database
        User.objects.create(username=username, password=password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")
    return render(request, "admin.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return render(request, "admindashboard.html", {"username": username})
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "Invalid username")
        return redirect("login")
    return render(request, "login.html")



def register_books(request):
    if request.method == "POST":
        sname = request.POST.get("sname")
        branch = request.POST.get("branch")
        books_name = request.POST.get("books_name")
        author = request.POST.get("author")
        course_enrolled = request.POST.get("course_enrolled")
        enrollment_date = request.POST.get("enrollment_date")
        category = request.POST.get("category")

        # Create and save new students
        Books.objects.create(
            sname=sname,
            branch=branch,
            books_name=books_name,
            author=author,
            course_enrolled=course_enrolled,
            enrollment_date=enrollment_date,
            category=category,

        )
        messages.success(request, "Books registered successfully!")
        return redirect("register_books")

    return render(request, "addbooks.html")

def list_books(request):
    books = Books.objects.all()  # Retrieve all students
    return render(request, "listbooks.html", {"books": books})



def delete_books(request,books_id):
    book = Books.objects.get(pk=books_id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect("list_books")

def update_books(request,books_id):
    book = Books.objects.get(pk=books_id)
    return render(request, "updatebooks.html", {"book": book})

def uprecc(request, books_id):
    sname = request.POST['sname']
    branch = request.POST['branch']
    books_id = request.POST['books_id']
    books_name = request.POST['books_name']
    author = request.POST['author']
    course_enrolled = request.POST['course_enrolled']
    enrollment_date = request.POST['enrollment_date']
    category = request.POST['category']

    book = Books.objects.get(pk=books_id)
    book.sname = sname
    book.branch = branch
    book.books_id = books_id
    book.books_name = books_name
    book.author = author
    book.course_enrolled = course_enrolled
    book.enrollment_date = enrollment_date
    book.category = category
    book.save()
    messages.success(request, "Books updated successfully!")
    return redirect("list_books")

