from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrdersView(ModelViewSet):
    # queryset - зріз даних які потрібно відображати
    queryset = SalesOrder.objects.all()
    # serializer_class - в ньому визначаєм які поля передаєм в запиті (з яких сформується словник а потім json): ['amount', 'description']
    serializer_class = OrderSerializer
