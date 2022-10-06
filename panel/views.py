from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.views import View

from map.models import User, Community, Event, City, Venue
from panel.forms import LoginForm, RegisterForm, AddLeadForm, AddCommunityForm, AddCityForm, EditLeadForm, AddEventForm, \
    AddVenueForm


class LoggedInView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect'


class LogoutView(LoggedInView):
    def get(self, request):
        logout(request)
        return redirect('index')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("panel_index")
        form = LoginForm()
        context = {"form": form}
        return render(request, "panel/login.html", context)

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
                    return render(request, "panel/login.html", context)
            else:
                form.add_error("email", "Invalid user and password combination!")
                context = {"form": form}
                return render(request, "panel/login.html", context)

        else:
            print("Errors")
            print(form.errors)
            # form.add_error("email", "Form is not valid")
            print("Form not valid!")
            print(form.non_field_errors)
            context = {"form": form}
            return render(request, "panel/login.html", context)


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "panel/register.html", context)

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
            return render(request, "panel/register.html", {'form': form})
        else:
            return render(request, "panel/register.html", {'form': form})


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

            user = get_user_model().objects.update_user(email, password, name, form.cleaned_data)
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
            form.save()
            return render(request, "panel/events/add_event.html", {'form': form})
        else:
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
