from django.conf.urls import include 
from django.urls import path 
from accounts import views 

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('user_edit/<int:id>', views.user_edit, name="user_edit"),
    path('user_info/<int:id>', views.user_info, name="user_info"),
    path('user_message/<int:id>', views.user_message, name="user_message"),
]