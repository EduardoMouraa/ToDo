from django import template
import pytz
from datetime import datetime, timedelta
register = template.Library()

@register.filter(name='convert_date')
def convert_date(date):
    # 2021-01-15 12:27:00+00:00
    debbug_Date = str(date).replace(' ', 'T').split("+")[0]
    return debbug_Date