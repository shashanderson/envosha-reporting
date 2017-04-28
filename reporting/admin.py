from django.contrib import admin
from .models import Customer, Company, AreaPersonalType , Parameter

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(AreaPersonalType)
admin.site.register(Parameter)