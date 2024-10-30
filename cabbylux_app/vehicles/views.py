from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm

def vehicle_list(request):
    vehicle = Vehicle.objects.all()
    return render(request, 'vehicle/vehicle_list.html', {'vehicle': vehicle})

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'vehicle/vehicle_detail.html', {'vehicle': vehicle})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle/vehicle_form.html', {'form': form})

def vehicle_update(request, driver_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_detail', vehicle_id=vehicle.id)
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle/vehicle_form.html', {'form': form})

def vehicle_delete(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicle/vehicle_confirm_delete.html', {'vehicle': vehicle})
