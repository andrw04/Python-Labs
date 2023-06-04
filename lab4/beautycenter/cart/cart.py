from decimal import Decimal
from django.conf import settings
from beautyapp.models import Service


class Cart(object):

    def __init__(self, request):
        """
        Initialize cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, service):
        service_id = str(service.id)
        if service_id not in self.cart:
            self.cart[service_id] = {'price': str(service.price)}

        self.save()

    def save(self):
        # Update session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark session as "changed" to be sure it is saved

    def remove(self, service):
        # Remove service from cart
        service_id = str(service.id)
        if service_id in self.cart:
            del self.cart[service_id]
            self.save()

    def get_total_price(self):
        # get total price of all services
        return sum(Decimal(item['price']) for item in self.cart.values())
    
    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def __iter__(self):
        # Iterate elements and get service from database
        service_ids = self.cart.keys()
        # getting service objects and adding them to cart
        services = Service.objects.filter(id__in=service_ids)
        for service in services:
            self.cart[str(service.id)]['service'] = service

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            yield item

        def __len__(self):
            # count of objects in cart
            return len(self.cart.values())
        
