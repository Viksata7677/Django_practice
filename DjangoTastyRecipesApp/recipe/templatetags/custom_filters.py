from django import template

register = template.Library()


@register.filter
def split_by_comma(value):
    """Splits a string by a comma and space."""
    if isinstance(value, str):
        return value.split(', ')  # Split string by ', ' and return list
    return value
