from django.shortcuts import render, redirect, get_object_or_404

from hotel_app.forms import ReservationForm, RoomTypeForm, RoomForm
from hotel_app.models import Room, Reservation, RoomType


# Create your views here.

def home(request):
    room_types = RoomType.objects.all()
    ctx = {
        'room_types':room_types
    }
    return render(request,'hotel_app/home.html', context=ctx)


def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.guest = request.user

            conflicting_reservations = Reservation.objects.filter(
                rooms__in=form.cleaned_data['rooms'],
                start__lte=reservation.end,
                end__gte=reservation.start
            )
            if conflicting_reservations.exists():
                error_message = "На указанные даты уже есть бронирование для этой комнаты."
                return render(request, 'hotel_app/reserve.html', {'form': form, 'error_message': error_message})

            reservation.save()
            form.save_m2m()

            return redirect('home')
    else:
        form = ReservationForm()

    return render(request, 'hotel_app/reserve.html', {'form': form})
def my_reserves(request):
    reservations = Reservation.objects.filter(guest=request.user)
    ctx = {
        'reservations': reservations
    }
    return render(request, 'hotel_app/my_reserves.html', context=ctx)


def reservation_edit(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)

            reservation.guest = request.user
            reservation.save()
            form.save_m2m()
            return redirect('my_reserves')
    else:
        form = ReservationForm(instance=reservation)
    ctx = {'form': form, 'reservation': reservation}
    return render(request, 'hotel_app/reservation_edit.html', context=ctx)
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('my_reserves')
    ctx = {'reservation': reservation}
    return render(request, 'hotel_app/reservation_delete.html', context=ctx)


def create_room_type(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST, request.FILES)
        if form.is_valid():
            room_type = form.save()
            return redirect('home')
    else:
        form = RoomTypeForm()
    ctx = {'form': form}
    return render(request, 'hotel_app/create_room_type.html',context=ctx )

def add_room(request):
    if request.method =='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('home')
    else:
        form = RoomForm()
    ctx = {'form':form}
    return render(request,'hotel_app/add_room.html',context=ctx)

def room_type_edit(request, room_type_id):
    room_type = get_object_or_404(RoomType, pk=room_type_id)

    if request.method == 'POST':
        form = RoomTypeForm(request.POST, request.FILES, instance=room_type)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomTypeForm(instance=room_type)

    context = {'form': form}
    return render(request, 'hotel_app/room_type_edit.html', context)


def room_type_delete(request, room_type_id):
    room_type = get_object_or_404(RoomType, pk=room_type_id)

    if request.method == 'POST':
        room_type.delete()
        return redirect('home')

    context = {'room_type': room_type}
    return render(request, 'hotel_app/room_type_delete.html', context)