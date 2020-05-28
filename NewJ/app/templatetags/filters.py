from django import template

register = template.Library()

@register.filter(name='add')
def add_one(valeu):
    return valeu + 1