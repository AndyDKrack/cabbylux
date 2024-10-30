from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
    payment =Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payment': payment})

def payment_detail(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'payment/payment_detail.html', {'payment': payment})

def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment/payment_form.html', {'form': form})

def payment_update(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_detail', payment_id=payment.id)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment/payment_form.html', {'form': form})

def payment_delete(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_list')
    return render(request, 'payment/payment_confirm_delete.html', {'payment': payment})
