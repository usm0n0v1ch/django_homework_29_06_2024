from django.urls import path

from hotel_app import views

urlpatterns =[
    path('', views.home,name='home'),
    path('reserve/', views.reserve, name='reserve'),
    path('my_reserves/',views.my_reserves,name='my_reserves'),
    path('reservation_edit/<int:reservation_id>/', views.reservation_edit,name='reservation_edit'),
    path('reservation_delete/<int:reservation_id>/',views.reservation_delete,name='reservation_delete'),
    path('create_room_type/',views.create_room_type,name='create_room_type'),
    path('add_room/',views.add_room,name='add_room'),
    path('room_type_edit/<int:room_type_id>/',views.room_type_edit,name='room_type_edit'),
    path('room_type_delete/<int:room_type_id>',views.room_type_delete,name='room_type_delete'),
]