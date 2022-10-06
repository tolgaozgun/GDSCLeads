from django.db.models.functions import Lead
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core import serializers

from map.models import Community, User, Event
import json

from map.serializers import LazyEncoder


class IndexView(View):
    def get(self, request):
        return render(request, "map/index.html")


class EventMapView(View):
    def get(self, request):

        events = Event.objects.all()
        json_events = serializers.serialize('json', events, cls=LazyEncoder)

        # leads = User.objects.all()
        # json_leads = serializers.serialize('json', leads, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "events": events,
                   "json_events": json_events}

        return render(request, "map/map_events.html", context)


class CommunityMapView(View):
    def get(self, request):
        communities = Community.objects.all()
        json_communities = serializers.serialize('json', communities, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "communities": communities,
                   "json_communities": json_communities}

        return render(request, "map/map_communities.html", context)


class LeadMapView(View):
    def get(self, request):
        leads = User.objects.filter(is_lead=True)
        json_leads = serializers.serialize('json', leads, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "leads": leads,
                   "json_leads": json_leads}

        return render(request, "map/map_leads.html", context)


class LeadApiView(View):
    def get(self, request, pk):
        try:
            lead = User.objects.get(id=pk)
            context = {"lead": lead}
        except User.DoesNotExist:
            context = {}
        return render(request, "map/lead_box_content.html", context)


class CommunityApiView(View):
    def get(self, request, pk):
        try:
            community = Community.objects.get(id=pk)
            context = {"community": community}
        except Community.DoesNotExist:
            context = {}
        return render(request, "map/community_box_content.html", context)


class EventApiView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
            context = {"event": event}
        except Event.DoesNotExist:
            context = {}
        return render(request, "map/event_box_content.html", context)

