from django.contrib import admin

# Register your models here.
from django.template.defaultfilters import date as _date
from django.template.defaultfilters import time as _time
from django.utils.translation import ugettext_lazy as _
from .models import*


admin.site.register(regdetails)
admin.site.register(cardio)
admin.site.register(neurologyform)
admin.site.register(nephrology)

