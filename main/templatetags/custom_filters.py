from django import template

register = template.Library()

@register.filter
def slice_list(value, arg):
    return value[:int(arg)]
