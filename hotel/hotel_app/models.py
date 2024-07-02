from django.contrib.auth.models import User
from django.db import models

class RoomType(models.Model):
    name = models.CharField(max_length=100)
    room_description = models.TextField(blank=True, null=True)
    place = models.IntegerField()
    area = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.IntegerField(unique=True, blank=True, null=True)
    room_type = models.ForeignKey(RoomType, related_name='rooms', on_delete=models.CASCADE)

    def __str__(self):
        return f'Комната {self.room_number} - {self.room_type.name}'

class Reservation(models.Model):
    rooms = models.ManyToManyField(Room, related_name='reservations')
    guest = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE, blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f'Бронирование для {self.guest} с {self.start} по {self.end}'
