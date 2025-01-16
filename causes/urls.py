from django.urls import path
from .views import welcome_view, RegisterView
urlpatterns = [
    path('', welcome_view, name= "welcome_view"),
    path('register/', RegisterView.as_view(), name='register')
]
