from django.shortcuts import render
from django.views import View
from django.conf import settings

from map.models import Community
import json


class IndexView(View):
    def get(self, request):
        data = Community.objects.values('name', 'latitude', 'longitude')
        json_data = json.dumps(list(data))
        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY, "data": json_data}
        return render(request, "map/index.html", context)
