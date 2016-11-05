from django import template
register = template.Library()

@register.filter(name='mul')
def mul(value,arg):
    sumPrice = value * arg
    if sumPrice:
        return sumPrice
    else:
        return -1
