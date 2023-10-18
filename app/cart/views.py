from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
import json

class Cart:
    def add(request, product_id):
        product = Product.objects.get(id=product_id)
        product_id_str = str(product_id)
        cart = request.session.get('cart', {})
        product_item = {}
        product_item['product'] = {
            'id': product.id,
            'title': product.title,
            'origil_price': str(product.origil_price),
            'sell_price': str(product.sell_price),
            'added_time': str(product.added_time),
        }

        if product_id_str in cart:
            item = cart[product_id_str]
            quantity = item['quantity'] + 1
            product_item.update({"quantity" : quantity})
        else:
            product_item['quantity'] = 1

        cart[product_id] = product_item
        request.session['cart'] = cart
        return HttpResponse()
