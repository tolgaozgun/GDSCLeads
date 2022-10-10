from datetime import datetime

from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from map.models import User, Community, Event, City, Venue
from panel.forms import AddLeadForm, AddCommunityForm, AddCityForm, EditLeadForm, AddEventForm, \
    AddVenueForm


class LoggedInView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect'


class LogoutView(LoggedInView):
    def get(self, request):
        logout(request)
        return redirect('index')


class IndexView(LoggedInView):
    def get(self, request):
        return render(request, "panel/index.html")


class NotFoundView(LoggedInView):
    def get(self, request):
        return render(request, "panel/404.html")


class ChartsView(LoggedInView):
    def get(self, request):
        return render(request, "panel/layout-static.html")


class AddMemberView(LoggedInView):
    def get(self, request):
        form = AddLeadForm()
        context = {"form": form}
        return render(request, "panel/members/add_member.html", context)

    def post(self, request):
        form = AddLeadForm(request.POST, request.FILES)

        if form.is_valid():
            email = form.cleaned_data.pop("email")
            password = form.cleaned_data.pop("password_again")
            name = form.cleaned_data.pop("name")
            form.cleaned_data.pop("password")

            user = get_user_model().objects.create_user(email, password, name, form.cleaned_data)
            return render(request, "panel/members/add_member.html", {'form': form})
        else:
            return render(request, "panel/members/add_member.html", {'form': form})


class BrowseMembersView(LoggedInView):
    def get(self, request):
        try:
            members = User.objects.all()
        except User.DoesNotExist:
            members = None
        context = {"members": members}
        return render(request, "panel/members/members.html", context)


class EditMemberView(LoggedInView):
    def get(self, request, pk):
        try:
            member = User.objects.get(id=pk)
        except User.DoesNotExist:
            member = None
        form = EditLeadForm(instance=member)
        context = {"form": form}
        return render(request, "panel/members/edit_member.html", context)

    def post(self, request, pk):
        try:
            member = User.objects.get(id=pk)
        except User.DoesNotExist:
            member = None
        form = EditLeadForm(request.POST, request.FILES, instance=member)

        if form.is_valid():
            email = form.cleaned_data.pop("email")
            password = form.cleaned_data.pop("password_again")
            name = form.cleaned_data.pop("name")
            form.cleaned_data.pop("password")

            if len(str(password).strip()) == 0:
                password = None

            user = get_user_model().objects.update_user_admin(pk, email, password, name, form.cleaned_data)
            return render(request, "panel/members/edit_member.html", {'form': form})
        else:
            return render(request, "panel/members/edit_member.html", {'form': form})


class DeleteMemberView(LoggedInView):
    def get(self, request):
        pass


class AddCommunityView(LoggedInView):
    def get(self, request):
        form = AddCommunityForm()
        context = {"form": form}
        return render(request, "panel/communities/add_community.html", context)

    def post(self, request):
        form = AddCommunityForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "panel/communities/add_community.html", {'form': form})
        else:
            return render(request, "panel/communities/add_community.html", {'form': form})


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
        form = AddEventForm()
        context = {"form": form}
        return render(request, "panel/events/add_event.html", context)

    def post(self, request):
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            draft = form.save(commit=False)
            cleaned_data = form.cleaned_data
            draft.latitude = cleaned_data.get("venue").latitude
            draft.longitude = cleaned_data.get("venue").longitude
            picked_date = cleaned_data.pop("picked_date")
            picked_time = cleaned_data.pop("picked_time")
            draft.date = datetime.combine(picked_date, picked_time)
            draft.save()
            form.save_m2m()
            return render(request, "panel/events/add_event.html", {'form': form})
        else:
            print("A")
            print(form.errors)
            return render(request, "panel/events/add_event.html", {'form': form})


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
        form = AddCityForm()
        context = {"form": form}
        return render(request, "panel/cities/add_city.html", context)

    def post(self, request):
        form = AddCityForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "panel/cities/add_city.html", {'form': form})
        else:
            return render(request, "panel/cities/add_city.html", {'form': form})


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


class AddVenueView(LoggedInView):
    def get(self, request):
        form = AddVenueForm()
        context = {"form": form}
        return render(request, "panel/venues/add_venue.html", context)

    def post(self, request):
        form = AddVenueForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "panel/venues/add_venue.html", {'form': form})
        else:
            return render(request, "panel/venues/add_venue.html", {'form': form})


class BrowseVenuesView(LoggedInView):
    def get(self, request):
        try:
            venues = Venue.objects.all()
        except Venue.DoesNotExist:
            venues = None
        context = {"venues": venues}
        return render(request, "panel/venues/venues.html", context)


class EditVenueView(LoggedInView):
    def get(self, request):
        pass


class DeleteVenueView(LoggedInView):
    def get(self, request):
        pass


class ProfileView(LoggedInView):
    def get(self, request):
        context = {'user': request.user}
        return render(request, "panel/settings/profile.html", context)