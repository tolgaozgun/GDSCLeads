from django.contrib import admin

# Register your models here.
from map.models import Lead, City, Community, Event

admin.site.register(Community)
admin.site.register(City)
admin.site.register(Lead)
admin.site.register(Event)