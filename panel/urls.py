
from django.urls import path, include

from panel.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="panel_index"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', RegisterView.as_view(), name="register"),
    path('forgot_password', ForgotPasswordView.as_view(), name="forgot_password"),
    path('404', NotFoundView.as_view(), name="not_found"),
    path('charts', ChartsView.as_view(), name="charts_view"),

    path('members', BrowseMembersView.as_view(), name="panel_members"),
    path('members/add', AddMemberView.as_view(), name="panel_member_add"),
    path('members/<int:pk>/edit', EditMemberView.as_view(), name="panel_member_edit"),
    path('members/<int:pk>/delete', DeleteMemberView.as_view(), name="panel_member_delete"),

    path('communities', BrowseCommunitiesView.as_view(), name="panel_communities"),
    path('communities/add', AddCommunityView.as_view(), name="panel_community_add"),
    path('communities/<int:pk>/edit', EditCommunityView.as_view(), name="panel_community_edit"),
    path('communities/<int:pk>/delete', DeleteCommunityView.as_view(), name="panel_community_delete"),

    path('events', BrowseEventsView.as_view(), name="panel_events"),
    path('events/add', AddEventView.as_view(), name="panel_event_add"),
    path('events/<int:pk>/edit', EditEventView.as_view(), name="panel_event_edit"),
    path('events/<int:pk>/delete', DeleteEventView.as_view(), name="panel_event_delete"),

    path('cities', BrowseCitiesView.as_view(), name="panel_cities"),
    path('cities/add', AddCityView.as_view(), name="panel_city_add"),
    path('cities/<int:pk>/edit', EditCityView.as_view(), name="panel_city_edit"),
    path('cities/<int:pk>/delete', DeleteCityView.as_view(), name="panel_city_delete"),

    path('venues', BrowseVenuesView.as_view(), name="panel_venues"),
    path('venues/add', AddVenueView.as_view(), name="panel_venue_add"),
    path('venues/<int:pk>/edit', EditVenueView.as_view(), name="panel_venue_edit"),
    path('venues/<int:pk>/delete', DeleteVenueView.as_view(), name="panel_venue_delete"),


]