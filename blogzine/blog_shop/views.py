# shop/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Product

class ShopHomeView(TemplateView):
    template_name = 'blog_shop/index_shop.html'
def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog_shop/shop-grid.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'blog_shop/shop-detail.html', {'product': product})



# shop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create()
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_list')  # Assuming you have a URL named 'product_list' for the product list view


def update_cart(request):
    cart, _ = Cart.objects.get_or_create()
    cart_items = cart.cartitem_set.all()

    if request.method == 'POST':
        for cart_item in cart_items:
            quantity = request.POST.get(f'quantity_{cart_item.id}', 0)
            cart_item.quantity = max(int(quantity), 0)
            cart_item.save()

    return render(request, 'blog_shop/my-cart.html', {'cart_items': cart_items})