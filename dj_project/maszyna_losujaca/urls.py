from django.urls import path
from .views import index
urlpatterns = [

    path('maszyna_losujaca/', index)
    ]