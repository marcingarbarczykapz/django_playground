from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from shop.models import Customer, Order
from shop.serializers import OrderSerializer


class CustomerListView(ListView):
    model = Customer
    paginate_by = 10
    template_name = 'shop/customer_list.html'
    context_object_name = 'customers'


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
