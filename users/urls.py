from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.CallbackView.as_view(), name="callback"),
    path('home', views.home, name='home'),
    path('profile', views.UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/update', views.UserProfileUpdateView.as_view(), name='profile_update')
]
