from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.index, name='index'),
    path('products/<int:product_id>/', views.show, name='show'),
]
