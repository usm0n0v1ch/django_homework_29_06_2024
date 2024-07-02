from django.urls import path

from user import views

urlpatterns =[
    path('register/', views.register,name='register'),
    path('',views.auth,name='auth'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view,name='logout')

]