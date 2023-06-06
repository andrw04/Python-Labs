from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cart.forms import CartAddServiceForm
from .models import Service, Category, Client, Doctor
from .forms import ServiceForm, CategoryForm, DoctorForm
from requests import get
import json


def service_list(request, category_slug=None):
    categories = Category.objects.all()
    services = Service.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        services = services.filter(category=category)

    sort = request.GET.get('sort')
    if sort == 'name_ascending':
        services = services.order_by('name')
    elif sort == 'name_descending':
        services = services.order_by('-name')
    elif sort == 'price_ascending':
        services = services.order_by('price')
    elif sort == 'price_descending':
        services = services.order_by('-price')

    context = {
        'categories': categories,
        'services': services,
        'cart_service_form': CartAddServiceForm()
    }
    return render(request, 'services/service_list.html', context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/category_list.html', context)


def client_list(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request,'clients/client_list.html', context)


def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors,
    }
    return render(request,'doctors/doctor_list.html', context)


def add_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            image = request.FILES.get('image')
            if image:
                service.image = image
            service.save()
            messages.success(request, ('Service successful created!'))
            return redirect('add_service')
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Category successful created!'))
            return redirect('add_category')
    else:
        form = CategoryForm()
    return render(request, 'categories/add_category.html', {'form': form})


def add_doctor(request):
    if request.method == "POST":

        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            image = request.FILES.get('image')
            if image:
                doctor.image = image
            doctor.save()
            messages.success(request, ('Doctor was successful created!'))
            return redirect('add_doctor')
    else:
        form = DoctorForm()
    return render(request, 'doctors/add_doctor.html', {'form': form})


def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    return redirect('service_list')


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('category_list')


def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('client_list')


def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    doctor.delete()
    return redirect('doctor_list')


def index(request):
    # first api
    key = '2862bdc96c3f4b79a0bbf519bcb8f1df'
    data = json.loads(get(f'https://api.ipgeolocation.io/ipgeo?apiKey={key}').text)['time_zone']
    result = json.loads(get('https://favqs.com/api/qotd').text)
    context = {
        'author': result.get('quote').get('author'),
        'quote': result.get('quote').get('body'),
        'name': data.get('name'),
        'current_time': data.get('current_time')
    }
    return render(request, 'beautyapp/index.html', context)
