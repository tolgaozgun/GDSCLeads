from django.shortcuts import render

# Create your views here.
from django.views import View

from map.models import Community, Lead


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

