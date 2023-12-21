from django.urls import path

from .views import Login, Logout, ProfileView, register

urlpatterns = [
    path('register/', register, name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
