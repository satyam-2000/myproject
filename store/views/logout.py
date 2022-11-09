from django.shortcuts import render,redirect
from store.models.product import Product
from store.middlewares.auth import auth_middleware


def logout(request):
    request.session.clear()
    return redirect('index')


@auth_middleware
def cart(request):
    cart=request.session.get('cart')
    if not cart:
        return redirect('index')
    else:

        ids=list(cart.keys())
        print(ids)
        products=Product.get_cart_product(ids)
        print(products)
        return render(request,'store/cart.html',{'products':products})