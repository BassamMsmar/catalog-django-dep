from django.urls import path

from .views import sections_list, add_section


urlpatterns = [
    path('', sections_list, name='sections_list'),
    path('section/add/', add_section, name='add_section'),
]
