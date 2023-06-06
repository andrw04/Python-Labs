from decimal import Decimal
from django.conf import settings
from beautyapp.models import Service


class Cart(object):

    def __init__(self, request):
        # init cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, service):
        # Add service to cart
        service_id = str(service.id)
        if service_id not in self.cart:
            self.cart[service_id] = {'price': str(service.price)}
        self.save()

    def save(self):
        # update session
        self.session[settings.CART_SESSION_ID] = self.cart
        # Marg session as "changed" to be sure it saved
        self.session.modified = True

    def remove(self, service):
        # Remove service from cart
        service_id = str(service.id)
        if service_id in self.cart:
            del self.cart[service_id]
            self.save()

    def __iter__(self):
        service_ids = self.cart.keys()
        services = Service.objects.filter(id__in=service_ids)
        for service in services:
            self.cart[str(service.id)]['service'] = service

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            yield item

    def __len__(self):
        return len(self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        # Remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
