from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core import serializers

from map.models import Community, Lead
import json

from map.serializers import LazyEncoder


class IndexView(View):
    def get(self, request):
        return render(request, "map/index.html")


class EventMapView(View):
    def get(self, request):
        communities = Community.objects.all()
        json_communities = serializers.serialize('json', communities, cls=LazyEncoder)

        leads = Lead.objects.all()
        json_leads = serializers.serialize('json', leads, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "communities": communities,
                   "leads": leads,
                   "json_communities": json_communities,
                   "json_leads": json_leads}

        return render(request, "map/map_events.html", context)



class CommunityMapView(View):
    def get(self, request):
        communities = Community.objects.all()
        json_communities = serializers.serialize('json', communities, cls=LazyEncoder)

        leads = Lead.objects.all()
        json_leads = serializers.serialize('json', leads, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "communities": communities,
                   "leads": leads,
                   "json_communities": json_communities,
                   "json_leads": json_leads}

        return render(request, "map/map_communities.html", context)


class LeadMapView(View):
    def get(self, request):
        communities = Community.objects.all()
        json_communities = serializers.serialize('json', communities, cls=LazyEncoder)

        leads = Lead.objects.all()
        json_leads = serializers.serialize('json', leads, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "communities": communities,
                   "leads": leads,
                   "json_communities": json_communities,
                   "json_leads": json_leads}

        return render(request, "map/map_leads.html", context)


class LeadApiView(View):
    def get(self, request, pk):
        try:
            lead = Lead.objects.get(id=pk)
            context = {"lead": lead}
        except Lead.DoesNotExist:
            context = {}
        return render(request, "map/lead_box_content.html", context)

