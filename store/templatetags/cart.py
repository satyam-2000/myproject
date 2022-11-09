from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    # print(cart)
    
    keys=cart.keys()
   
    return False
@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    # print(cart)
    
    keys=cart.keys()
    for id in keys:
       
        
        if int(id)==product.id:
            q=cart.get(id)
            return q
    return 0
@register.filter(name='price_total')
def price_total(product,cart):
    return product.price * cart_quantity(product,cart)

@register.filter(name='cart_total')
def cart_total(products,cart):
    s=0
    for p in products:
        s+=s+price_total(p,cart)
    return s


@register.filter(name='multiply')
def multiply(num1,num2):
    return num1*num2
    
        
    
         
            
            
       
    

