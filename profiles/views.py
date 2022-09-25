from django.shortcuts import render

# Create your views here.
from django.views import View

from map.models import Community, Lead, Event, City


class CommunityView(View):
    def get(self, request, pk):
        try:
            community = Community.objects.get(id=pk)
        except Community.DoesNotExist:
            community = None
        context = {
            "community": community
        }
        return render(request, "profile/community_profile.html", context)


class LeadView(View):
    def get(self, request, pk):
        try:
            lead = Lead.objects.get(id=pk)
        except Lead.DoesNotExist:
            lead = None
        context = {
            "lead": lead
        }
        return render(request, "profile/lead_profile.html", context)


class EventView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            event = None
        context = {
            "event": event
        }
        return render(request, "profile/event_profile.html", context)


class CityView(View):
    def get(self, request, pk):
        try:
            city = City.objects.get(id=pk)
        except City.DoesNotExist:
            city = None
        context = {
            "city": city
        }
        return render(request, "profile/city_profile.html", context)

