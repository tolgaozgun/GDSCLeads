from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.core import serializers
from django.contrib import messages

from map.forms import RegisterForm
from map.models import Community, User, Event

from map.serializers import LazyEncoder
from panel.forms import LoginForm


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("panel_index")
        form = LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self, request):
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            value_email = form.cleaned_data.get("email")
            value_password = form.cleaned_data.get("password")

            user = authenticate(request, email=value_email, password=value_password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirection = request.POST.get("redirect", None)
                    if redirection is not None:
                        print("Redirect")
                        print(redirection)
                        return redirect(redirection)
                    return redirect("panel_index")
                else:
                    form.add_error("email", "Account has not been activated yet!")
                    context = {"form": form}
                    return render(request, "login.html", context)
            else:
                form.add_error("email", "Invalid user and password combination!")
                context = {"form": form}
                return render(request, "login.html", context)

        else:
            context = {"form": form}
            return render(request, "login.html", context)


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            name = form.cleaned_data.get("name")

            user = get_user_model().objects.create_user(email, password, name)
            # send_email(new_user)
            # new_user.save()
            messages.info(request, "Register successful!")
            return render(request, "register.html", {'form': form})
        else:
            return render(request, "register.html", {'form': form})


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, "password.html")


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

        return render(request, "map/events/map_events.html", context)


class CommunityMapView(View):
    def get(self, request):
        communities = Community.objects.all()
        json_communities = serializers.serialize('json', communities, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "communities": communities,
                   "json_communities": json_communities}

        return render(request, "map/communities/map_communities.html", context)


class LeadMapView(View):
    def get(self, request):
        leads = User.objects.filter(is_lead=True)
        json_leads = serializers.serialize('json', leads, cls=LazyEncoder)

        context = {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                   "leads": leads,
                   "json_leads": json_leads}

        return render(request, "map/leads/map_leads.html", context)


class LeadApiView(View):
    def get(self, request, pk):
        try:
            lead = User.objects.get(id=pk)
            context = {"lead": lead}
        except User.DoesNotExist:
            context = {}
        return render(request, "map/leads/lead_box_content.html", context)


class CommunityApiView(View):
    def get(self, request, pk):
        try:
            community = Community.objects.get(id=pk)
            context = {"community": community}
        except Community.DoesNotExist:
            context = {}
        return render(request, "map/communities/community_box_content.html", context)


class EventApiView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
            context = {"event": event}
        except Event.DoesNotExist:
            context = {}
        return render(request, "map/events/event_box_content.html", context)

