from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('',views.home,name='home'),
    path("register/", views.register_view, name="register"),
    path('register_student/',views.register_student,name='register_student'),
    path("students/", views.list_student, name="list_student"),
    path("delete_student/<student_id>", views.delete_student, name="delete_student"),
    path("update_student/<student_id>", views.update_student, name="update_student"),
    path("update/uprec/<student_id>", views.uprec, name="uprec"),

    path("login/", views.login_view, name="login"),

    path('register_books/', views.register_books, name='register_books'),
    path("list_books/", views.list_books, name="list_books"),
    path("delete_books/<books_id>", views.delete_books, name="delete_books"),
    path("update_books/<books_id>", views.update_books, name="update_books"),
    path("updatebooks/uprecc/<books_id>", views.uprecc, name="uprecc"),

    ]