from django.urls import path
from .views import * 
urlpatterns = [
    path('calculator',calculator),
    path('',index)
]
