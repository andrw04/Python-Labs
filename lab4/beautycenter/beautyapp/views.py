from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, SignupForm, OrderCreateForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from cart.forms import CartAddServiceForm
from cart.cart import Cart

# Create your views here.


def index(request):
    return render(request, 'beautyapp/index.html', {})


def create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'beautyapp/category_form.html', context)


# def create_planned_visit(request):
#     form = ScheduleForm()
#     context = {'form': form}
#     return render(request, 'beautyapp/planned_visit_form.html', context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username OR password does not exist...')
    context = {'page': page}
    return render(request, 'beautyapp/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def registerPage(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'An error occured during registration...')

    return render(request, 'beautyapp/login_register.html', {'form': form})


def service_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    services = Service.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        services = services.filter(category=category)
    
    context = {
        'category': category,
        'categories': categories,
        'services': services 
    }
    return render(request, 'service/list.html', context)


def service_detail(request, id, slug):
    service = get_object_or_404(Service, id=id, slug=slug, available=True)
    cart_service_form = CartAddServiceForm()
    context = {'service': service,
               'cart_service_form': cart_service_form}

    return render(request, 'service/detail.html', context)


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, service=item['service'], price=item['price'])

            # clear cart
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart, 'form': form})




# def order_create(request):
#     if request.method == "POST":
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in
