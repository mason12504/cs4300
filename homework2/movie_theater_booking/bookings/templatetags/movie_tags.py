# found this idea on stackoverflow https://stackoverflow.com/questions/60866618/how-to-get-model-field-value-from-model-and-field-in-django-template
# But I am pretty sure it is UNNECESSARY. Keeping it for the time being though. 


from django import template

register = template.Library()

@register.filter
def value_from_model(model, field):
    return getattr(model, field)