from django.urls import path

from .views import base


urlpatterns = [
    path('home/', base, {'name': 'Home'}, name='home'),
    path('company/', base, {'name': 'About company'}, name='company'),
    path('development/', base, {'name': 'Development'}, name='development'),
    path('development/cpp', base, {'name': 'Development C++'}, name='development_cpp'),
    path('development/cpp/qt', base, {'name': 'Development C++/Qt'}, name='development_cpp_qt'),
    path('development/python', base, {'name': 'Development Python'}, name='development_python'),
    path('development/python/django', base, {'name': 'Development Python/Django'}, name='development_python_django'),
    path('development/python/tornado', base, {'name': 'Development Python/Tornado'}, name='development_python_tornado'),
    path('prices/', base, {'name': 'Prices'}, name='prices'),
]

