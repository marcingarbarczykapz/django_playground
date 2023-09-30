from django.urls import path

from shop import views

urlpatterns = [
    path('customers/', views.CustomerListView.as_view(), name='customers'),
]
