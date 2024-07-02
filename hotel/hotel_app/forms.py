from django import forms

from hotel_app.models import Reservation, Room, RoomType




class ReservationForm(forms.ModelForm):
    start = forms.DateTimeField(widget=forms.SelectDateWidget)
    end = forms.DateTimeField(widget=forms.SelectDateWidget)
    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all())

    class Meta:
        model = Reservation
        fields = ['start', 'end', 'rooms']
        exclude = ['guest']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type']

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['name', 'room_description', 'place', 'area', 'price', 'image']