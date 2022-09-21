from django.contrib import admin

# Register your models here.
from map.models import Lead, City, Community

admin.site.register(Community)
admin.site.register(City)
admin.site.register(Lead)