from django.urls import path
from . import views  # Импортируем views из текущего пакета

urlpatterns = [
    path('', views.index, name='index'),  # путь при переходе на главную страницу
    path('about/', views.about, name='about'),  # путь при переходе на главную страницу
    path('courses_online/', views.courses_online, name='courses_online'),  # путь при переходе на страницу онлайн курсов
    path('courses_2_4/', views.courses_2_4, name='courses_2_4'),
    path('courses_4_6/', views.courses_4_6, name='courses_4_6'),
    path('courses_6_7/', views.courses_6_7, name='courses_6_7'),
    path('courses_7_9/', views.courses_7_9, name='courses_7_9'),
    path('courses_9_11/', views.courses_9_11, name='courses_9_11'),
    path('courses_11_13/', views.courses_11_13, name='courses_11_13'),
    path('courses_13_16/', views.courses_13_16, name='courses_13_16'),
    path('about-cookies/', views.about_cookies, name='about_cookies'),
]
