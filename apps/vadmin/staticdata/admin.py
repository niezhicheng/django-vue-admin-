from django.contrib import admin
from apps.vadmin.staticdata.models.data import Country,SiteArea,Region
# Register your models here.
admin.site.register(Country)
admin.site.register(SiteArea)
admin.site.register(Region)