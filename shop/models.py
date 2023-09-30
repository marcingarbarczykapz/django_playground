from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.name} (${self.price})'


class Customer(models.Model):
    STATE_CHOICES = [
        ('NY', 'New York'),
        ('CA', 'California'),
        ('TX', 'Texas'),
        # add more as needed
    ]

    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('UK', 'United Kingdom'),
        # add more as needed
    ]

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    STATUS_CHOICES = (('P', 'Pending'), ('D', 'Delivered'), ('C', 'Cancelled'))

    placed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f'Order #{self.pk} - {self.get_status_display()}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
