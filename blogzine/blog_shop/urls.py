
from django.urls import path
from . import views
from .views import ShopHomeView

urlpatterns = [
    path('' , ShopHomeView.as_view ,name='shop-index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
]
