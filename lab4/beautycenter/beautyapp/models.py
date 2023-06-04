from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Gender(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'

    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    gender = models.CharField(max_length=6, choices=GENDERS)


class Client(models.Model) :

    first_name = models.CharField(max_length=200,
                                help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self) :
        return '{0}, {1}'.format(self.first_name, self.last_name) 
    

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_list_by_category', args=[self.slug])


class Service(models.Model):
    category = models.ForeignKey(
        Category, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(
        upload_to='images/', blank=True, null=True, default='images/no_image.png')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.id, self.slug])


class Order(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.price

# class Category(models.Model):
#     name = models.CharField(max_length=80)


# class Service(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=200)
#     gender = models.CharField(max_length=10)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)


# class PriceList(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     price = models.IntegerField()


# class Sale(models.Model):
#     order_number = models.IntegerField()
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)


# class Office(models.Model):
#     number = models.IntegerField()


# class Doctor(models.Model):
#     fullname = models.CharField(max_length=80)
#     office_id = models.OneToOneField(Office, on_delete=models.CASCADE)
#     # client_id = models.ManyToManyField(Client, through="PlannedVisit")


# class Order(models.Model):
#     number = models.IntegerField()
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     created = models.DateTimeField()


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)


# class Visit(models.Model):
#     date = models.DateTimeField()
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     comments = models.CharField(max_length=2000)


# class Schedule(models.Model):
#     visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
