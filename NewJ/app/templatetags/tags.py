from django import template

register = template.Library()

@register.simple_tag(name='qwe')
def app_tag():
    return 'Hello!!!!'