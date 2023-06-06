from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from beautyapp.models import Client, Service
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            Client.objects.create(first_name=order.first_name,
                                  last_name=order.last_name,
                                  email=order.email,
                                  address=order.address,
                                  mobile=order.mobile)
            for item in cart:
                OrderItem.objects.create(order=order,
                                         service=item['service'],
                                         price=item['price'])

            # Clear cart
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_list(request):
    orders = Order.objects.all()
    orderItems = OrderItem.objects.all()
    services = Service.objects.all()

    context = {
        'orders': orders,
        'orderItems': orderItems,
        'services': services,
    }
    return render(request, 'orders/order_list.html', context)


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('orders:order_list')
