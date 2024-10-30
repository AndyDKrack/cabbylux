from django.shortcuts import render, get_object_or_404, redirect
from .models import Driver
from .forms import DriverForm

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'drivers/driver_detail.html', {'driver': driver})

def driver_create(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm()
    return render(request, 'drivers/driver_form.html', {'form': form})

def driver_update(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_detail', driver_id=driver.id)
    else:
        form = DriverForm(instance=driver)
    return render(request, 'drivers/driver_form.html', {'form': form})

def driver_delete(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')
    return render(request, 'drivers/driver_confirm_delete.html', {'driver': driver})
