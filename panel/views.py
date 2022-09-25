from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View

from map.models import Lead, Community, Event, City


class LoggedInView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect'


class LoginView(View):
    def get(self, request):
        return render(request, "panel/login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "panel/register.html")


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, "panel/password.html")


class IndexView(LoggedInView):
    def get(self, request):
        return render(request, "panel/index.html")


class NotFoundView(LoggedInView):
    def get(self, request):
        return render(request, "panel/404.html")


class ChartsView(LoggedInView):
    def get(self, request):
        return render(request, "panel/layout-static.html")


class AddLeadView(LoggedInView):
    def get(self, request):
        pass


class BrowseLeadsView(LoggedInView):
    def get(self, request):
        try:
            leads = Lead.objects.all()
        except Lead.DoesNotExist:
            leads = None
        context = {"leads": leads}
        return render(request, "panel/leads/leads.html", context)


class EditLeadView(LoggedInView):
    def get(self, request):
        pass


class DeleteLeadView(LoggedInView):
    def get(self, request):
        pass


class AddCommunityView(LoggedInView):
    def get(self, request):
        pass


class BrowseCommunitiesView(LoggedInView):
    def get(self, request):
        try:
            communities = Community.objects.all()
        except Community.DoesNotExist:
            communities = None
        context = {"communities": communities}
        return render(request, "panel/communities/communities.html", context)


class EditCommunityView(LoggedInView):
    def get(self, request):
        pass


class DeleteCommunityView(LoggedInView):
    def get(self, request):
        pass


class AddEventView(LoggedInView):
    def get(self, request):
        pass


class BrowseEventsView(LoggedInView):
    def get(self, request):
        try:
            events = Event.objects.all()
        except Event.DoesNotExist:
            events = None
        context = {"events": events}
        return render(request, "panel/events/events.html", context)


class EditEventView(LoggedInView):
    def get(self, request):
        pass


class DeleteEventView(LoggedInView):
    def get(self, request):
        pass


class AddCityView(LoggedInView):
    def get(self, request):
        pass


class BrowseCitiesView(LoggedInView):
    def get(self, request):
        try:
            cities = City.objects.all()
        except City.DoesNotExist:
            cities = None
        context = {"cities": cities}
        return render(request, "panel/cities/cities.html", context)


class EditCityView(LoggedInView):
    def get(self, request):
        pass


class DeleteCityView(LoggedInView):
    def get(self, request):
        pass