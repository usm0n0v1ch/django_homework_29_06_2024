from django.contrib import admin

from hotel_app.models import Reservation, Room, RoomType

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(RoomType)