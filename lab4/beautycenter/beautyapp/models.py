from django.db import models

# Create your models here.


class Client(models.Model):
    fullname = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    birth_date = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=80)


class Service(models.Model):
    name = models.CharField(max_length=80)


class PriceList(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.FloatField()


class Sale(models.Model):
    order_number = models.IntegerField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    get_date = models.DateTimeField()
    order_id = models.ForeignKey(PriceList, on_delete=models.CASCADE)


class Office(models.Model):
    number = models.IntegerField()


class Doctor(models.Model):
    fullname = models.CharField(max_length=80)
    office_id = models.OneToOneField(Office, on_delete=models.CASCADE)
    client_id = models.ManyToManyField(Client, through="PlannedVisit")


class PlannedVisit(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)


class Schedule(models.Model):
    date_time = models.DateTimeField()
    visit = models.ForeignKey(PlannedVisit, on_delete=models.CASCADE)
