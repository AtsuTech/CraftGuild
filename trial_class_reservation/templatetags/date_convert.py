from django import template
from datetime import datetime
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def date_m_d(date): 

    date_string = date
    date_object = datetime.strptime(date_string, "%Y-%m-%d")

    formatted_date = date_object.strftime("%-m/%-d")

    return (formatted_date)



