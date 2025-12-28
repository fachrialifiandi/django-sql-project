from django.shortcuts import render
from django.db import connection
from store.models import Product, Collection, Order, OrderItem


def say_hello(request):

    query_set = 1

    return render(request, 'hello.html', {'name': 'Alif', 'result': list(query_set)})
    # return render(request, 'hello.html', {'name': 'Alif', 'result': result})
