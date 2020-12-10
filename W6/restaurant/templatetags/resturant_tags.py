from django import template

from restaurant.models import Product

register = template.Library()


@register.filter(is_safe=True)
def comma_seperator(value, arg):
    temp = []

    while True:
        temp.append(str(value % 1000))
        value //= 1000
        if not value:
            break
    temp = temp[::-1]

    res = ",".join(temp)
    return res


@register.simple_tag
def get_object_by_name(data):
    product = Product.objects.get(name=data)
    suppliers = product.supplier.all()

    temp = ''
    for e in suppliers:
        temp = temp + e.account.name + ' '

    return temp
