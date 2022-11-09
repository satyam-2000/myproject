from django.conf.urls import url
from store import views
from store.views import login,signup

from store.views import logout
from .views import checkout
from .views import order
from .views import contact


# SET THE NAMESPACE!
app_name = 'store'

urlpatterns=[
   
    url('signup/',signup.Signup.as_view(),name='signup'),
    url('login/',login.Login.as_view(),name='login'),
    url('logout/',logout.logout,name='logout'),
    url('cart/',logout.cart,name='cart'),
    url('checkout/',checkout.Checkout.as_view(),name='checkout'),
    url('order/',order.Orders.as_view(),name='order'),
    url('contact/',contact.Contact.as_view(),name='contact'),
    
    
]
