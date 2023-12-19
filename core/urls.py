from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('upload', views.upload, name = "upload"),
    path('signup', views.signup, name = "signup"),
    path('signin', views.signin, name = "signin"),
    path('settings',views.settings,name = "settings"),
    path('profile/<str:pk>', views.profile, name = "profile"),
    path('logout', views.logout, name = "logout"),
    path('like-post', views.like_post, name = "like_post"),
    path('contact', views.contactus, name = "contactus"),
    path('message', views.message, name = "message"),
]