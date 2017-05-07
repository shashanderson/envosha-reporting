from django import template

from reporting.models import Company

register = template.Library()


@register.simple_tag
def get_obj(pk, attr):
    obj = getattr(Company.objects.get(pk=int(pk)), attr)
    return obj