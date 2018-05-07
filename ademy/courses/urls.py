from django.urls import path, include

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name='list'),
    path('<int:course_pk>/<int:lesson_pk>/', views.lesson_detail, name='lesson_detail'),
    path('<int:pk>/', views.course_detail, name='detail'),
]
