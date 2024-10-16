from django.urls import path
from api.views import *

urlpatterns = [
    path('section/', section_view, name='section'),
    path('section/<int:pk>/', section_view, name='section'),
]
