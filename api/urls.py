from django.urls import path
from api.views import test

urlpatterns = [
    path("", test)
]
