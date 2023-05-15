from django.urls import path
from .views import home, RegisterView
from .views import profile

urlpatterns = [
    path('dashboard/', home, name='index'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]